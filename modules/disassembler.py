import subprocess, os

def disassemble_list(scripts):

    for script_name in scripts:
        try:    
            print ("Working on: " + script_name)
            return_code = subprocess.check_output(['disassembler', script_name])
            
            out_script = os.path.join(r"C:\PycDc_output", scripts + ".py")
            
            print ("I am writting down: " +  out_script)
            with open(out_script, 'w') as f:
                for s in return_code:
                    f.write(s)   #f.write((s + u'\n').encode('unicode-escape'))
        except:
            pass    


