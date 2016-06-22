import subprocess

#Executing an External Command and Getting Its Output
#https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch13s06.html
try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output       # Output generated before error
    code      = e.returncode   # Return code