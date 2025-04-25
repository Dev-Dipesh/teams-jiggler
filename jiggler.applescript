set scriptPath to POSIX path of (path to me)
set scriptDir to do shell script "dirname " & quoted form of scriptPath
set pyScript to scriptDir & "/jiggler.py"
set venvPython to scriptDir & "/venv/bin/python"

repeat
    do shell script quoted form of venvPython & " " & quoted form of pyScript
    delay 240
end repeat
