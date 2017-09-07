#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def totalHammingDistance(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		res = 0
		for i in range(32):
			mask = 1 << i
			zero = one = 0
			for num in nums:
				if num & mask:
					one += 1
				else:
					zero += 1
			res += one * zero
		return res


nums = [441593, 6015010, 6681906, 6272231, 3575648, 7354199, 7517847, 8389024, 7705777, 1884575, 1829787, 1223874,
		8480137, 7283234, 8456893, 5661683, 3238113, 5341883, 7434585, 3035703, 3471728, 5138738, 1485018, 5643252,
		7499409, 5950490, 6155822, 8739187, 8764556, 3280230, 1733988, 825682, 2289046, 315500, 1872095, 384627,
		9107850, 1900523, 5195445, 9199478, 607541, 6106887, 2901042, 3860371, 886232, 3540272, 9337233, 6081312,
		2239464, 3512582, 3723669, 4297609, 4206423, 4926298, 1911900, 5844084, 680362, 8754875, 8234350, 3125330,
		5341627, 6247661, 8459902, 7486257, 966605, 2903217, 1317062, 4430652, 1082677, 6499627, 5048639, 1164061,
		8091427, 7191628, 9341274, 4516553, 3015604, 1560057, 9158790, 3344258, 2278740, 1988691, 7248776, 7446199,
		4461289, 7081490, 2575689, 7887438, 7317154, 3650221, 9889540, 6693361, 2871727, 9864409, 896577, 4950511,
		5867234, 6951143, 9668152, 6761426, 2167804, 7475608, 859662, 3300262, 4473591, 2633091, 9924475, 7737681,
		9528702, 9821212, 1894289, 2711474, 3197530, 7859115, 5049426, 3443258, 5832626, 103955, 5612727, 2953222,
		9945917, 8250465, 7130001, 9380111, 2349900, 3606832, 3675641, 9031035, 9711399, 6559866, 7178865, 330712,
		1095088, 3976083, 6020392, 7532223, 3789099, 255153, 3375198, 1813364, 6759223, 4103427, 2394729, 4496767,
		4793835, 9792950, 4071855, 7001103, 6016449, 4682289, 1270664, 6787222, 9840685, 5756933, 4239705, 1701606,
		384787, 3093479, 2617136, 2930457, 3642563, 3168002, 4130839, 7443725, 285505, 6142974, 9505895, 6199564,
		8583359, 6805518, 6563202, 7536083, 954986, 1133395, 2687965, 2754145, 3270940, 9795380, 6392910, 5382510,
		7397107, 2882756, 342679, 4178458, 7820456, 207725, 1322471, 2621338, 6543780, 7172308, 4416279, 7789399,
		7103526, 430119, 8408470, 8993322, 664497, 8433800, 3936277, 971638, 178758, 7329569, 4263127, 1110292, 8640712,
		9789477, 905655, 5921301, 4447099, 634805, 5462135, 9513790, 4478652, 8687676, 9327180, 2875673, 2032855,
		382123, 6976676, 1700948, 7813269, 9585373, 3496574, 5074504, 8395717, 6730763, 1136296, 4040338, 1539752,
		703924, 3114055, 3368299, 8977539, 9811793, 4107310, 174911, 7436062, 8210487, 3130912, 9585811, 9301330,
		705590, 9355783, 8933916, 1495946, 3067081, 5221484, 9906173, 2473280, 549200, 28323, 2163105, 588358, 7864161,
		1992837, 9493397, 5536880, 6057404, 8995840, 8358591, 1715525, 2808908, 7655100, 8722637, 3113328, 6265725,
		8641483, 5863342, 8118232, 4250729, 97642, 885558, 6808067, 1312, 8876939, 372796, 4462655, 7398140, 3055656,
		378509, 3685110, 130519, 5019986, 9990381, 487244, 8306321, 664815, 6554980, 9395375, 1059704, 8791508, 6169602,
		6524537, 9803007, 9589143, 3438897, 8982390, 6275129, 6220555, 4843361, 4388386, 6045637, 98671, 1523363,
		5772155, 3112614, 2966770, 7252110, 2916137, 7729345, 6298151, 35641, 7415131, 8240081, 3293824, 910036,
		7171257, 6921679, 8788237, 6217128, 101239, 8835715, 4056763, 9151437, 8984032, 6221267, 7544102, 6936184,
		3840062, 3367979, 7537520, 5016001, 756086, 2486699, 1746821, 6463467, 467385, 9117842, 5684091, 3053433,
		8267505, 3644392, 4732806, 1820147, 287148, 7314032, 444610, 4307751, 9944193, 4816574, 331700, 3852827,
		4061757, 6461464, 8392141, 6415176, 8612814, 5412860, 3946379, 632841, 1414631, 1508012, 6943097, 8514341,
		6257640, 8175154, 2372382, 5186272, 7703046, 6625923, 3595485, 8463791, 8603812, 5672956, 6869379, 3643693,
		6135, 2669456, 7904718, 855534, 4576210, 7057956, 8045840, 4568076, 168530, 6071086, 3654059, 5816674, 428002,
		7421516, 6591332, 3860171, 1553697, 6420494, 1582064, 3351972, 2051049, 5604081, 1914987, 4613873, 6976796,
		9779567, 9617730, 436341, 8432357, 9727974, 9685158, 1238313, 1721010, 9848969, 1092098, 5145021, 9069867,
		3002088, 4001602, 5468846, 2949080, 8546879, 2299005, 1283789, 9242454, 2124570, 1938503, 8165216, 2398305,
		4902998, 218156, 7019600, 4985725, 8454820, 3292927, 8994023, 675739, 2264227, 9839165, 3065760, 591480,
		9466616, 8802234, 2898306, 5281153, 5876476, 5397105, 7932250, 8518437, 4093023, 773480, 9725521, 4654208,
		5205519, 8682753, 2692296, 2262285, 9200418, 558097, 6186581, 9506831, 1886718, 8839298, 5879400, 9426906,
		9307421, 4543093, 3271806, 4870644, 2108966, 2920854, 8397365, 2611788, 9275709, 8095244, 486679, 8979923,
		5681259, 7105611, 2831002, 7646003, 5782912, 9402692, 2997967, 8555065, 8628796, 555821, 5078382, 1449705,
		7544196, 3325510, 510527, 3685034, 7893544, 3697629, 7837463, 5602885, 1035460, 6910423, 5105824, 1233800,
		8331443, 2188579, 5219165, 5863319, 4130316, 593686, 7184123, 6501695, 9545314, 1783919, 8061998, 7037048,
		2692884, 9886401, 7874409, 6782041, 6125508, 3392034, 9141747, 3438292, 2966131, 1275459, 9363255, 823821,
		569730, 1442211, 1455448, 8005018, 4014099, 4481348, 7372969, 4983436, 2093176, 2333813, 2317178, 2823377,
		1660384, 8254344, 4050621, 946066, 4939421, 6408382, 4732703, 5890604, 4493755, 1011285, 7134685, 6287188,
		9370124, 5797148, 4331632, 961315, 4558787, 9759241, 2501469, 9175389, 7865028, 3878596, 139918, 9036779,
		2863207, 5922881, 3766982, 4029665, 5669352, 5688153, 7599001, 1837879, 7562984, 1904447, 1101915, 1909805,
		2540974, 540658, 8189196, 4424076, 8131888, 7310299, 5322568, 7663294, 7645060, 6864689, 2867110, 2389601,
		691982, 4189305, 295542, 9811610, 3018097, 3673663, 3665479, 1049570, 5263058, 2669256, 3764963, 8142331,
		6991755, 2368878, 2920923, 5312180, 6141400, 5251900, 4481506, 6654854, 7320201, 1441083, 5138864, 4641256,
		2667589, 1502826, 8394842, 986082, 1031511, 876446, 670126, 4260247, 9897111, 8520892, 5489050, 1797530, 28387,
		9467841, 215610, 4228978, 23516, 9905790, 7639355, 2967222, 1168606, 6691196, 729440, 3699465, 4464226, 8441848,
		4099125, 778726, 1057157, 2517566, 1060623, 5196784, 925696, 5605855, 3503318, 3046844, 8304537, 4788905,
		2080774, 8091821, 5721141, 2943762, 3242564, 7645218, 377463, 8395855, 1873129, 4954044, 5550764, 841639,
		2418367, 2254589, 9061412, 3020213, 5954298, 2143346, 2042023, 8239611, 3700734, 2372242, 3871848, 755147,
		7406616, 6548096, 5512898, 8749310, 4261906, 465834, 5782541, 7275073, 6608609, 9269664, 9275731, 2923621,
		748110, 569356, 4591793, 8519948, 9929889, 7557381, 8299426, 1620684, 4132112, 8397547, 8096371, 9779013,
		6549719, 8285590, 2025143, 9209829, 1797996, 6347937, 559855, 6160797, 8966412, 509437, 9961117, 5487330,
		3928046, 8785644, 1124065, 7832656, 399459, 5701116, 8765098, 6801801, 5940961, 8720296, 3905231, 3867873,
		2650813, 2922215, 1622537, 7396793, 7391603, 9080519, 2899251, 903567, 4371463, 5468353, 127941, 2762563,
		5697930, 8333664, 950525, 4036058, 7651791, 8131497, 7532450, 1621422, 9955745, 5109482, 7444361, 117489,
		179000, 3992129, 3154446, 6645992, 1854811, 2931442, 8210990, 1552366, 5653533, 5436262, 514303, 5377801,
		2237611, 4063011, 2254018, 2761571, 6339476, 3502162, 2488752, 6648883, 4888492, 6629569, 8203230, 4062178,
		4192455, 5663301, 8231616, 1069015, 9005951, 369032, 9779239, 1995455, 8043390, 5038280, 403750, 9423109,
		8054041, 2142082, 2187376, 2235521, 1454982, 2677578, 991105, 8917337, 9341982, 1471599, 6722519, 2456277,
		2398268, 5793651, 1923731, 3254102, 4282761, 4428353, 7894117, 2289484, 2516653, 5151232, 9441010, 305549,
		5494637, 7898462, 6489297, 698172, 8484836, 5557637, 6186593, 9845605, 1302840, 2546031, 510434, 9266516,
		8014649, 6446916, 5714795, 6546741, 6800745, 7809457, 4478533, 9756865, 4858904, 8475054, 4267231, 9398509,
		6555842, 9898342, 1805575, 7011167, 7971118, 2428157, 2459607, 2517554, 4369650, 6737508, 7062310, 5895896,
		276533, 678192, 3154932, 8097171, 2051215, 7095286, 641682, 9622006, 3613561, 371299, 8614865, 6891460, 3416105,
		9855467, 1860694, 5271288, 9738555, 7046069, 3621120, 4164902, 6643610, 2540715, 3669044, 5852658, 4646490,
		2789204, 1636306, 4139998, 9606325, 4781818, 5655475, 503413, 1908082, 4913737, 7060728, 3368554, 1964567,
		9031885, 1051238, 9967711, 9474802, 6337890, 1102859, 4278881, 4161503, 3378173, 6179920, 6700384, 6539309,
		775900, 4733973, 5251274, 7120190, 1540523, 6684897, 4251101, 378711, 851036, 4475503, 6845187, 3967796,
		7856004, 8350672, 7277937, 5659302, 3966534, 1331927, 2709997, 3169080, 8310564, 113559, 1745979, 4298441,
		3854335, 5805358, 713946, 1644453, 7251517, 2949586, 3631154, 7478718, 3998431, 5652093, 5829895, 3502348,
		1249123, 7772659, 900680, 3863186, 6348559, 235454, 9868396, 2397176, 8172316, 7055627, 324205, 2679851,
		5513148, 1529192, 626738, 2428886, 4375044, 2234153, 5821294, 2456052, 1913649, 1301306, 5681339, 4205303,
		8621059, 5420174, 9131177, 8383568, 8694943, 8134226, 3152531, 6537699, 4878297, 6443871, 1454279, 3290214,
		2176788, 1336894, 5853500, 7115915, 650241, 6328586, 2167732, 250171, 7261213, 901014, 9081681, 9652431,
		9501824, 2190444, 9556777, 7906825, 8482085, 1398692, 5619438, 7561910, 7884842, 9441314, 9917698, 5486244,
		3247687, 8036545, 5614655, 1191163, 8311317, 7397410, 5242921, 4442700, 411299, 7779197, 3257001, 2499831,
		5369989, 4498484, 1179299, 7096158, 8413054, 9547321, 843190, 3599891]
t = time.time()
print(Solution().totalHammingDistance(nums))
print(time.time() - t)
