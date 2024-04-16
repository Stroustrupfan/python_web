import os
import subprocess

def compare_foundry_vs_halmos(filepath):
  script_dir = os.path.dirname(os.path.realpath(__file__))
  for address in os.listdir(filepath):
    if address.endswith(".bin"):
      address = os.path.join(filepath, address)
      filename = os.path.splitext(os.path.basename(address))[0]

    #   # Use Foundry to represent fuzz testing
    #   forge_dir = os.path.join(script_dir, '../Dataset/forge')
    #   forge_report = f"forge_report_{filename}.txt"
    #   forge_command = f"forge test {filepath} > {os.path.join(forge_dir, forge_report)}"
    #   subprocess.run(forge_command, shell= True)

      # Use Halmos to represent formal verification
      halmos_dir = os.path.join(script_dir, '../Dataset/halmos')
      halmos_report = f"halmos_report_{filename}.txt"
      halmos_command = f"halmos test {filepath} > {os.path.join(halmos_dir, halmos_report)}"
      subprocess.run(halmos_command, shell= True)
      
path_to_binaries = '../Dataset/SC_Bins'

compare_foundry_vs_halmos(path_to_binaries)