"""import subprocess      
import argparse         
import os               
import pickle     
import pathlib as path  


def ValidatePath(thePath):
    ''' Validate the Folder thePath
        it must exist and we must have rights
        to read from the folder.
        raise the appropriate error if either
        is not true
    '''
    # Validate the path exists
    if not os.path.exists(thePath):
        raise argparse.ArgumentTypeError('Path does not exist')

    # Validate the path is readable
    if os.access(thePath, os.R_OK):
        valores(thePath)
    else:
        raise argparse.ArgumentTypeError('Path is not readable')
def valores(targetPath):
    try:
        print()
        command = "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder "+ targetPath + " -ResultFile " + tmpFile 

        powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
        if powerShellResult.stderr == None:
            input("ya")
        
            baseDict = {}
            
            with open(tmpFile, 'r') as inFile:
                for eachLine in inFile:
                    lineList = eachLine.split()
                    if len(lineList) == 2:
                        hashValue = lineList[0]
                        fileName  = lineList[1]
                        baseDict[hashValue] = fileName
                    else:
                        continue
        
            with open(baselineFile, 'wb') as outFile:
                pickle.dump(baseDict, outFile)
                print("Baseline: ", baselineFile, " Created with:",
                      "{:,}".format(len(baseDict)), "Records")
                print("Script Terminated Successfully")
        else:
            print("PowerShell Error:", p.stderr)
            
    except Exception as err:
        if os.path.exists('Reportes/r_logs_baseline.txt'):
            with open('Reportes/r_logs_baseline.txt','a') as fa:
                fa.write("Cannot Create Output File: "+str(err))
        else:
            with open('Reportes/r_logs_baseline.txt','w') as fa:
                fa.write("Cannot Create Output File: "+str(err))

        quit()
    """
"""def EnlistarArch(path):
    arc_list = os.listdir("Ruta")"""

    


"""import subprocess       # subprocess library
import argparse         # argument parsing library
import os               # Operating System Path
import pickle           # Python object serialization 

'''ARGUMENT PARSING SECTION '''

def ValidatePath(thePath):
    ''' Validate the Folder thePath
        it must exist and we must have rights
        to read from the folder.
        raise the appropriate error if either
        is not true
    '''
    # Validate the path exists
    if not os.path.exists(thePath):
        raise argparse.ArgumentTypeError('Path does not exist')

    # Validate the path is readable
    if os.access(thePath, os.R_OK):
        return thePath
    else:
        raise argparse.ArgumentTypeError('Path is not readable')

#End ValidatePath ===================================

''' Specify and Parse the command line, validate the arguments and return results'''
info = 'File System Baseline Creator with PowerShell- Version 1.0 December 2018'
parser = argparse.ArgumentParser(info)
parser.add_argument('-b', '--baseline',   required=True,
                    help="Specify the resulting baseline file")
parser.add_argument('-p', '--Path',       type= ValidatePath,
                    required=True, help="Specify the target folder to baseline")
parser.add_argument('-t', '--tmp',        required=True,
                    help="Specify a temporary result file for the PowerShell Script")

args = parser.parse_args()   

baselineFile = args.baseline
targetPath   = args.Path
tmpFile      = args.tmp

''' MAIN SCRIPT SECTION '''
if __name__ == '__main__':

    try:
        ''' POWERSHELL EXECUTION SECTION '''
        print()
        command = "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder "+\
                  targetPath + " -ResultFile " + tmpFile 
        print(command)
        powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
        if powerShellResult.stderr == None:
            input("ya")
        
            ''' DICTIONARY CREATION SECTION '''
            baseDict = {}
            
            with open(tmpFile, 'r') as inFile:
                for eachLine in inFile:
                    lineList = eachLine.split()
                    if len(lineList) == 2:
                        hashValue = lineList[0]
                        fileName  = lineList[1]
                        baseDict[hashValue] = fileName
                    else:
                        continue
        
            with open(baselineFile, 'wb') as outFile:
                pickle.dump(baseDict, outFile)
                print("Baseline: ", baselineFile, " Created with:",
                      "{:,}".format(len(baseDict)), "Records")
                print("Script Terminated Successfully")
        else:
            print("PowerShell Error:", p.stderr)
            
    except Exception as err:
        print ("Cannot Create Output File: "+str(err))
        quit()



  

    """



"""import subprocess
import argparse
import os
import pickle
import pathlib as path

def validate_path(target_path: str) -> None:
    
    if not target_path.exists():
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
            print(f"Error de PowerShell: {power_shell_result.stderr.decode('utf-8')}")
        else:
            base_dict = {}

            with open(tmp_file, "r") as in_file:
                for line in in_file:
                    line_list = line.split()
                    if len(line_list) == 2:
                        hash_value = line_list[0]
                        file_name = line_list[1]
                        base_dict[hash_value] = file_name

            with open(baseline_file, "wb") as out_file:
                pickle.dump(base_dict, out_file)
                print(f"Archivo de hash: {baseline_file} creado con {len(base_dict):,} registros")
                print("Script terminado exitosamente")

    except Exception as err:
        error_file = "Reportes/r_logs_baseline.txt"

        with open(error_file, "a" if error_file.exists() else "w") as fa:
            fa.write(f"Error al crear archivo de salida: {err}\n")
        quit()

if __name__ == "__main__":
    # Reemplaza esta ruta con la ruta adecuada al directorio que quieres analizar
    ruta_directorio = path.Path("C:/Users/Usuario/Desktop/Proyect_P_CIB")
    validate_path(ruta_directorio)

    # Obtener todos los subdirectorios
    subdirectorios = [d for d in ruta_directorio.glob("**/*") if d.is_dir()]

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
            with open(error_file, "a") as fa:
                fa.write(f"Error al crear archivo de salida: {err}\n")"""

import subprocess
import argparse
import os
import pickle
import pathlib as path

def validate_path(target_path: str) -> None:
    
    if not target_path.exists():
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
            print(f"Error de PowerShell: {power_shell_result.stderr.decode('utf-8')}")
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

        with open(error_file, "a" if error_file.exists() else "w") as fa:
            fa.write(f"Error al crear archivo de salida: {err}\n")
        quit()

if __name__ == "__main__":
    # Reemplaza esta ruta con la ruta adecuada al directorio que quieres analizar
    ruta_directorio = path.Path("C:/Users/Usuario/Desktop/Proyect_P_CIB")
    validate_path(ruta_directorio)

    # Obtener todos los subdirectorios
    subdirectorios = [d for d in ruta_directorio.glob("**/*") if d.is_dir()]

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
            with open(error_file, "a") as fa:
                fa.write(f"Error al crear archivo de salida: {err}\n")