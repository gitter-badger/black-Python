import subprocess,os

if not os.path.exists(r"C:\PycDc_output"):
    os.mkdir(r"C:\PycDc_output")

##for scripts_ in os.listdir("/source"):
##    if scripts_.endswith(".pyc"):
##        print ("I got the files!")
##        scripts.append(scripts_)


def ping(test_scripts):
    for test_script_name in test_scripts:
        print ("Working on: " + test_script_name)
        return_code = subprocess.check_output(['ping', test_script_name])
        out_script = os.path.join(r"C:\PycDc_output", test_script_name + ".py")
        #out_script = test_script_name + ".py"

        print ("I am writting down: " +  out_script)
        with open(out_script, 'w') as f:
            for s in return_code:
                f.write(s)   #f.write((s + u'\n').encode('unicode-escape'))
        


