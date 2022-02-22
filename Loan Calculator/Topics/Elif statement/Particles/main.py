spin = input()
elec_charge = input()

if spin == "1/2":
    if elec_charge == "-1/3":
        print("Strange Quark")
    elif elec_charge == "2/3":
        print("Charm Quark")
    elif elec_charge == "-1":
        print("Electron Lepton")
    elif elec_charge == "0":
        print("Neutrino Lepton")
else:
    print("Photon Boson")