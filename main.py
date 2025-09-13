import asf_search as asf

results = asf.search(polarization=asf.POLARIZATION.DUAL_VV)
print("Polarization using constants:", len(results))

results = asf.search(polarization='Dual VV')
print("Polarization using strings:", len(results))

