import os
import subprocess

def bill_fuzz(file_path, aflplusplus_path, output_dir):
    cmd = f"{aflplusplus_path} -i {file_path} -o {output_dir} -- ../smart_contracts @@"
    process = subprocess.Popen(cmd, shell = True)
    process.communicate()
    
def main():
    file_path = "../smart_contracts/USDC.abi"
    aflplusplus_path = sys.argv[1]
    output_dir = "../output"
    log_file = "../output/log.txt"
    bill_fuzz(file_path, aflplusplus_path, output_dir)
    
if __name__ == "__main__":
    main()