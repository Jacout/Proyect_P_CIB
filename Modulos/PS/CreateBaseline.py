import subprocess
import argparse
import os
import pickle
import pathlib as path

#editar por favor
def validate_path(target_path: str) -> None:
    

    if not os.path.exists(target_path):
        raise argparse.ArgumentTypeError(f"El directorio '{target_path}' no existe")

    if not os.access(target_path, os.R_OK):
        raise argparse.ArgumentTypeError(f"No se tienen permisos de lectura en el directorio '{target_path}'")

    valores(target_path)

def valores(target_path: str) -> None:
  
  
    try:
        tmp_file = "tmp.txt"
        baseline_file = "baseline.pkl"

        command = (
            "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 "
            f"-TargetFolder {target_path} -ResultFile {tmp_file}"
        )

        power_shell_result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if power_shell_result.stderr:
            if os.path.exists('Reportes/r_logs_baseline.txt'):
                with open('Reportes/r_logs_baseline.txt',"a") as f:
                    f.write(f"Error de PowerShell: {power_shell_result.stderr.decode('utf-8')}")
            else:
                with open('Reportes/r_logs_baseline.txt',"w") as f:
                    f.write(f"Error de PowerShell: {power_shell_result.stderr.decode('utf-8')}")
        else:
            base_dict = {}

            with open(tmp_file, "r") as in_file:
                for line in in_file:
                    line_list = line.split()
                    if len(line_list) == 2:
                        hash_value = line_list[0]
                        file_name = line_list[1]
                        base_dict[hash_value] = file_name

            with open(baseline_file, "ab") as out_file:
                pickle.dump(base_dict, out_file)
                print(f"Archivo de hash: {baseline_file} actualizado con {len(base_dict):,} registros")
                print("Script terminado exitosamente")

    except Exception as err:
        error_file = "Reportes/r_logs_baseline.txt"

        with open(error_file, "a" if os.path.exists(error_file) else "w") as fa:
            fa.write(f"Error al crear archivo de salida: {err}\n")
        quit()

def sacar_hash(path):
    # Reemplaza esta ruta con la ruta adecuada al directorio que quieres analizar
    validate_path(path)

    # Obtener todos los subdirectorios
    subdirectorios = [d for d in path.glob("**/*") if d.is_dir()]

    # Generar hash para cada subdirectorio
    for subdir in subdirectorios:
        print(f"Generando hash para el directorio: {subdir}")
        ruta_directorio = subdir
        error_file = "Reportes/r_logs_baseline.txt"
        try:
            valores(ruta_directorio)
        except Exception as err:
            if not os.path.isfile(error_file):
                open(error_file, "w").close()
            else:
                with open(error_file, "a") as fa:
                    fa.write(f"Error al crear archivo de salida: {err}\n")