import subprocess       # subprocess library
import os               # Operating System Path
import pickle           # Python object serialization 

def obtener(path,carpeta):

    try:
        baselineFile = f'Reportes/hashes_{carpeta}.pickle'
        targetPath   = path
        tmpFile      = os.path.abspath(f'Reportes/hashes_{carpeta}.txt')
        
        command = "powershell -ExecutionPolicy ByPass -File Modulos/HashAcquire.ps1 -TargetFolder "+\
                  targetPath + " -ResultFile " + tmpFile 

        powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
    
        if powerShellResult.stderr == None:
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
        else:
            if os.path.exists('Reportes/r_logs_baseline.txt'):
                with open('Reportes/r_logs_baseline.txt',"a") as f:
                    f.write(f"Error de PowerShell: {power_shell_result.stderr.decode('utf-8')}")
            else:
                with open('Reportes/r_logs_baseline.txt',"w") as f:
                    f.write(f"Error de PowerShell: {power_shell_result.stderr.decode('utf-8')}")
            
    except Exception as err:
        error_file = "Reportes/r_logs_baseline.txt"
        with open(error_file, "a" if os.path.exists(error_file) else "w") as fa:
            fa.write(f"Error al crear archivo de salida: {err}\n")
    
    
    
    
