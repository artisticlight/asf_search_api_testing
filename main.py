import asf_search as asf
import asf_search.constants as c

results = asf.search(polarization=c.POLARIZATION.DUAL_VV)
print("Polarization using constants:", len(results))

results = asf.search(polarization='Dual VV')
print("Polarization using strings:", len(results))

