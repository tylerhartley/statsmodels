from datetime import datetime

from numpy.testing import assert_almost_equal, assert_equal
from numpy import array, column_stack
from statsmodels.datasets import macrodata
from statsmodels.tsa.base.datetools import dates_from_range
from pandas import Series, Index, DataFrame
from statsmodels.tsa.filters import bkfilter, hpfilter, cffilter

def test_bking1d():
    """
    Test Baxter King band-pass filter. Results are taken from Stata
    """
    bking_results = array([7.320813, 2.886914, -6.818976, -13.49436,
                -13.27936, -9.405913, -5.691091, -5.133076, -7.273468,
                -9.243364, -8.482916, -4.447764, 2.406559, 10.68433,
                19.46414, 28.09749, 34.11066, 33.48468, 24.64598, 9.952399,
                -4.265528, -12.59471, -13.46714, -9.049501, -3.011248,
                .5655082, 2.897976, 7.406077, 14.67959, 18.651, 13.05891,
                -2.945415, -24.08659, -41.86147, -48.68383, -43.32689,
                -31.66654, -20.38356, -13.76411, -9.978693, -3.7704, 10.27108,
                31.02847, 51.87613, 66.93117, 73.51951, 73.4053, 69.17468,
                59.8543, 38.23899, -.2604809, -49.0107, -91.1128, -112.1574,
                -108.3227, -86.51453, -59.91258, -40.01185, -29.70265,
                -22.76396, -13.08037, 1.913622, 20.44045, 37.32873, 46.79802,
                51.95937, 59.67393, 70.50803, 81.27311, 83.53191, 67.72536,
                33.78039, -6.509092, -37.31579, -46.05207, -29.81496, 1.416417,
                28.31503,
                32.90134, 8.949259, -35.41895, -84.65775, -124.4288, -144.6036,
                -140.2204, -109.2624, -53.6901, 15.07415, 74.44268, 104.0403,
                101.0725, 76.58291, 49.27925, 36.15751, 36.48799, 37.60897,
                27.75998, 4.216643, -23.20579, -39.33292, -36.6134, -20.90161,
                -4.143123, 5.48432, 9.270075, 13.69573, 22.16675, 33.01987,
                41.93186, 47.12222, 48.62164, 47.30701, 40.20537, 22.37898,
                -7.133002, -43.3339, -78.51229, -101.3684, -105.2179,
                -90.97147,
                -68.30824, -48.10113, -35.60709, -31.15775, -31.82346,
                -32.49278, -28.22499, -14.42852, 10.1827, 36.64189, 49.43468,
                38.75517, 6.447761, -33.15883, -62.60446, -72.87829, -66.54629,
                -52.61205, -38.06676, -26.19963, -16.51492, -7.007577,
                .6125674,
                7.866972, 14.8123, 22.52388, 30.65265, 39.47801, 49.05027,
                59.02925,
                72.88999, 95.08865, 125.8983, 154.4283, 160.7638, 130.6092,
                67.84406, -7.070272, -68.08128, -99.39944, -104.911,
                -100.2372, -98.11596, -104.2051, -114.0125, -113.3475,
                -92.98669, -51.91707, -.7313812, 43.22938, 64.62762, 64.07226,
                59.35707, 67.06026, 91.87247, 124.4591, 151.2402, 163.0648,
                154.6432])
    X = macrodata.load().data['realinv']
    Y = bkfilter(X, 6, 32, 12)
    assert_almost_equal(Y,bking_results,4)

def test_bking2d():
    """
    Test Baxter-King band-pass filter with 2d input
    """
    bking_results = array([[7.320813,-.0374475], [2.886914,-.0430094],
        [-6.818976,-.053456], [-13.49436,-.0620739], [-13.27936,-.0626929],
        [-9.405913,-.0603022], [-5.691091,-.0630016], [-5.133076,-.0832268],
        [-7.273468,-.1186448], [-9.243364,-.1619868], [-8.482916,-.2116604],
        [-4.447764,-.2670747], [2.406559,-.3209931], [10.68433,-.3583075],
        [19.46414,-.3626742], [28.09749,-.3294618], [34.11066,-.2773388],
        [33.48468,-.2436127], [24.64598,-.2605531], [9.952399,-.3305166],
        [-4.265528,-.4275561], [-12.59471,-.5076068], [-13.46714,-.537573],
        [-9.049501,-.5205845], [-3.011248,-.481673], [.5655082,-.4403994],
        [2.897976,-.4039957], [7.406077,-.3537394], [14.67959,-.2687359],
        [18.651,-.1459743], [13.05891,.0014926], [-2.945415,.1424277],
        [-24.08659,.2451936], [-41.86147,.288541], [-48.68383,.2727282],
        [-43.32689,.1959127], [-31.66654,.0644874], [-20.38356,-.1158372],
        [-13.76411,-.3518627], [-9.978693,-.6557535], [-3.7704,-1.003754],
        [10.27108,-1.341632], [31.02847,-1.614486], [51.87613,-1.779089],
        [66.93117,-1.807459], [73.51951,-1.679688], [73.4053,-1.401012],
        [69.17468,-.9954996], [59.8543,-.511261], [38.23899,-.0146745],
        [-.2604809,.4261311], [-49.0107,.7452514], [-91.1128,.8879492],
        [-112.1574,.8282748], [-108.3227,.5851508], [-86.51453,.2351699],
        [-59.91258,-.1208998], [-40.01185,-.4297895], [-29.70265,-.6821963],
        [-22.76396,-.9234254], [-13.08037,-1.217539], [1.913622,-1.57367],
        [20.44045,-1.927008], [37.32873,-2.229565], [46.79802,-2.463154],
        [51.95937,-2.614697], [59.67393,-2.681357], [70.50803,-2.609654],
        [81.27311,-2.301618], [83.53191,-1.720974], [67.72536,-.9837123],
        [33.78039,-.2261613], [-6.509092,.4546985], [-37.31579,1.005751],
        [-46.05207,1.457224], [-29.81496,1.870815], [1.416417,2.263313],
        [28.31503,2.599906], [32.90134,2.812282], [8.949259,2.83358],
        [-35.41895,2.632667], [-84.65775,2.201077], [-124.4288,1.598951],
        [-144.6036,.9504762], [-140.2204,.4187932], [-109.2624,.1646726],
        [-53.6901,.2034265], [15.07415,.398165], [74.44268,.5427476],
        [104.0403,.5454975], [101.0725,.4723354], [76.58291,.4626823],
        [49.27925,.5840143], [36.15751,.7187981], [36.48799,.6058422],
        [37.60897,.1221227], [27.75998,-.5891272], [4.216643,-1.249841],
        [-23.20579,-1.594972], [-39.33292,-1.545968], [-36.6134,-1.275494],
        [-20.90161,-1.035783], [-4.143123,-.9971732], [5.48432,-1.154264],
        [9.270075,-1.29987], [13.69573,-1.240559], [22.16675,-.9662656],
        [33.01987,-.6420301], [41.93186,-.4698712], [47.12222,-.4527797],
        [48.62164,-.4407153], [47.30701,-.2416076], [40.20537,.2317583],
        [22.37898,.8710276], [-7.133002,1.426177], [-43.3339,1.652785],
        [-78.51229,1.488021], [-101.3684,1.072096], [-105.2179,.6496446],
        [-90.97147,.4193682], [-68.30824,.41847], [-48.10113,.5253419],
        [-35.60709,.595076], [-31.15775,.5509905], [-31.82346,.3755519],
        [-32.49278,.1297979], [-28.22499,-.0916165], [-14.42852,-.2531037],
        [10.1827,-.3220784], [36.64189,-.2660561], [49.43468,-.1358522],
        [38.75517,-.0279508], [6.447761,.0168735], [-33.15883,.0315687],
        [-62.60446,.0819507], [-72.87829,.2274033], [-66.54629,.4641401],
        [-52.61205,.7211093], [-38.06676,.907773], [-26.19963,.9387103],
        [-16.51492,.7940786], [-7.007577,.5026631], [.6125674,.1224996],
        [7.866972,-.2714422], [14.8123,-.6273921], [22.52388,-.9124271],
        [30.65265,-1.108861], [39.47801,-1.199206], [49.05027,-1.19908],
        [59.02925,-1.139046], [72.88999,-.9775021], [95.08865,-.6592603],
        [125.8983,-.1609712], [154.4283,.4796201], [160.7638,1.100565],
        [130.6092,1.447148], [67.84406,1.359608], [-7.070272,.8931825],
        [-68.08128,.2619787], [-99.39944,-.252208], [-104.911,-.4703874],
        [-100.2372,-.4430657], [-98.11596,-.390683], [-104.2051,-.5647846],
        [-114.0125,-.9397582], [-113.3475,-1.341633], [-92.98669,-1.567337],
        [-51.91707,-1.504943], [-.7313812,-1.30576], [43.22938,-1.17151],
        [64.62762,-1.136151], [64.07226,-1.050555], [59.35707,-.7308369],
        [67.06026,-.1766731], [91.87247,.3898467], [124.4591,.8135461],
        [151.2402,.9644226], [163.0648,.6865934], [154.6432,.0115685]])

    X = macrodata.load().data[['realinv','cpi']].view((float,2))
    Y = bkfilter(X, 6, 32, 12)
    assert_almost_equal(Y,bking_results,4)

def test_hpfilter():
    """
    Test Hodrick-Prescott Filter. Results taken from Stata.
    """
    hpfilt_res = array([[3.951191484487844718e+01,2.670837085155121713e+03],
        [8.008853245681075350e+01,2.698712467543189177e+03],
        [4.887545512195401898e+01,2.726612544878045810e+03],
        [3.059193256079834100e+01,2.754612067439201837e+03],
        [6.488266733421960453e+01,2.782816332665780465e+03],
        [2.304024204546703913e+01,2.811349757954532834e+03],
        [-1.355312369487364776e+00,2.840377312369487299e+03],
        [-6.746236512580753697e+01,2.870078365125807522e+03],
        [-8.136743836853429457e+01,2.900631438368534418e+03],
        [-6.016789026443257171e+01,2.932172890264432681e+03],
        [-4.636922433138215638e+01,2.964788224331382025e+03],
        [-2.069533915570400495e+01,2.998525339155703932e+03],
        [-2.162152558595607843e+00,3.033403152558595593e+03],
        [-4.718647774311648391e+00,3.069427647774311481e+03],
        [-1.355645669169007306e+01,3.106603456691690099e+03],
        [-4.436926204475639679e+01,3.144932262044756499e+03],
        [-4.332027378211660107e+01,3.184407273782116590e+03],
        [-4.454697106352068658e+01,3.224993971063520803e+03],
        [-2.629875787765286077e+01,3.266630757877652741e+03],
        [-4.426119635629265758e+01,3.309228196356292756e+03],
        [-1.443441190762496262e+01,3.352680411907625057e+03],
        [-2.026686669186437939e+01,3.396853866691864368e+03],
        [-1.913700136208899494e+01,3.441606001362089046e+03],
        [-5.482458977940950717e+01,3.486781589779409387e+03],
        [-1.596244517937793717e+01,3.532213445179378141e+03],
        [-1.374011542874541192e+01,3.577700115428745448e+03],
        [1.325482813403914406e+01,3.623030171865960710e+03],
        [5.603040174253828809e+01,3.667983598257461836e+03],
        [1.030743373627105939e+02,3.712348662637289181e+03],
        [7.217534795943993231e+01,3.755948652040559864e+03],
        [5.462972503693208637e+01,3.798671274963067845e+03],
        [4.407065050666142270e+01,3.840449349493338559e+03],
        [3.749016270204992907e+01,3.881249837297949853e+03],
        [-1.511244199923112319e+00,3.921067244199923152e+03],
        [-9.093507374079763395e+00,3.959919507374079785e+03],
        [-1.685361946760258434e+01,3.997823619467602384e+03],
        [2.822211031434289907e+01,4.034790889685657021e+03],
        [6.117590627896424849e+01,4.070822093721035344e+03],
        [5.433135391434370831e+01,4.105935646085656117e+03],
        [3.810480376716623141e+01,4.140188196232833434e+03],
        [7.042964928802848590e+01,4.173670350711971878e+03],
        [4.996346842507591646e+01,4.206496531574924120e+03],
        [4.455282059571254649e+01,4.238825179404287155e+03],
        [-7.584961950576143863e+00,4.270845961950576566e+03],
        [-4.620339247697120300e+01,4.302776392476971523e+03],
        [-7.054024364552969928e+01,4.334829243645529459e+03],
        [-6.492941099801464588e+01,4.367188410998014660e+03],
        [-1.433567024239555394e+02,4.399993702423955256e+03],
        [-5.932834493089012540e+01,4.433344344930889747e+03],
        [-6.842096758743628016e+01,4.467249967587436004e+03],
        [-6.774011924654860195e+01,4.501683119246548813e+03],
        [-9.030958565658056614e+01,4.536573585656580690e+03],
        [-4.603981499136807543e+01,4.571808814991368308e+03],
        [2.588118806672991923e+01,4.607219811933269739e+03],
        [3.489419371912299539e+01,4.642608806280876706e+03],
        [7.675179642495095322e+01,4.677794203575049323e+03],
        [1.635497817724171910e+02,4.712616218227582976e+03],
        [1.856079654765617306e+02,4.746963034523438182e+03],
        [1.254269446392718237e+02,4.780825055360728584e+03],
        [1.387413113837174024e+02,4.814308688616282780e+03],
        [6.201826599282230745e+01,4.847598734007177882e+03],
        [4.122129542972197669e+01,4.880966704570278125e+03],
        [-4.120287475842360436e+01,4.914722874758424041e+03],
        [-9.486328233441963675e+01,4.949203282334419782e+03],
        [-1.894232132641573116e+02,4.984718213264157384e+03],
        [-1.895766639620087517e+02,5.021518663962008759e+03],
        [-1.464092413342650616e+02,5.059737241334265491e+03],
        [-1.218770668721217589e+02,5.099388066872122181e+03],
        [-4.973075629078175552e+01,5.140393756290781312e+03],
        [-5.365375213897277717e+01,5.182600752138972894e+03],
        [-7.175241524251214287e+01,5.225824415242512259e+03],
        [-7.834757283225462743e+01,5.269846572832254424e+03],
        [-6.264220687943907251e+01,5.314404206879438789e+03],
        [-3.054332122210325906e+00,5.359185332122210639e+03],
        [4.808218808024685131e+01,5.403838811919753425e+03],
        [2.781399326736391231e+00,5.448011600673263274e+03],
        [-2.197570415173231595e+01,5.491380704151732061e+03],
        [1.509441335012807031e+02,5.533624866498719712e+03],
        [1.658909029574851957e+02,5.574409097042514986e+03],
        [2.027292548049981633e+02,5.613492745195001589e+03],
        [1.752101578176061594e+02,5.650738842182393455e+03],
        [1.452808749847536092e+02,5.686137125015246056e+03],
        [1.535481629475025329e+02,5.719786837052497503e+03],
        [1.376169777998875361e+02,5.751878022200112355e+03],
        [1.257703080340770612e+02,5.782696691965922582e+03],
        [-2.524186846895645431e+01,5.812614868468956047e+03],
        [-6.546618027042404719e+01,5.842083180270424236e+03],
        [1.192352023580315290e+01,5.871536479764196883e+03],
        [1.043482970188742911e+02,5.901368702981125352e+03],
        [2.581376184768396342e+01,5.931981238152316109e+03],
        [6.634330880534071184e+01,5.963840691194659485e+03],
        [-4.236780162594641297e+01,5.997429801625946311e+03],
        [-1.759397735321817891e+02,6.033272773532181418e+03],
        [-1.827933311233055065e+02,6.071867331123305121e+03],
        [-2.472312362505917918e+02,6.113601236250591683e+03],
        [-2.877470049336488955e+02,6.158748004933649099e+03],
        [-2.634066336693540507e+02,6.207426633669354487e+03],
        [-1.819572770763625158e+02,6.259576277076362203e+03],
        [-1.175034606274621183e+02,6.314971460627461965e+03],
        [-4.769898649718379602e+01,6.373272986497183410e+03],
        [1.419578280287896632e+01,6.434068217197121157e+03],
        [6.267929662760798237e+01,6.496914703372392069e+03],
        [6.196413196753746888e+01,6.561378868032462378e+03],
        [5.019769125317907310e+01,6.627066308746821051e+03],
        [4.665364933213822951e+01,6.693621350667861407e+03],
        [3.662430749527266016e+01,6.760719692504727391e+03],
        [7.545680850246480986e+01,6.828066191497535328e+03],
        [6.052940492147536133e+01,6.895388595078524304e+03],
        [6.029518881462354329e+01,6.962461811185376064e+03],
        [2.187042136652689805e+01,7.029098578633473153e+03],
        [2.380067926824722235e+01,7.095149320731752596e+03],
        [-7.119129802169481991e+00,7.160478129802169860e+03],
        [-3.194497359120850888e+01,7.224963973591208742e+03],
        [-1.897137038934124575e+01,7.288481370389341464e+03],
        [-1.832687287845146784e+01,7.350884872878451461e+03],
        [4.600482336597542599e+01,7.412017176634024509e+03],
        [2.489047706403016491e+01,7.471709522935970199e+03],
        [6.305909392127250612e+01,7.529821906078727807e+03],
        [4.585212309498183458e+01,7.586229876905018500e+03],
        [9.314260180878318351e+01,7.640848398191216802e+03],
        [1.129819097095369216e+02,7.693621090290463144e+03],
        [1.204662123176703972e+02,7.744549787682329224e+03],
        [1.336860614601246198e+02,7.793706938539875409e+03],
        [1.034567175813735957e+02,7.841240282418626521e+03],
        [1.403118873372050075e+02,7.887381112662795204e+03],
        [1.271726169351004501e+02,7.932425383064899506e+03],
        [8.271925765282139764e+01,7.976756742347178260e+03],
        [-3.197432211752584408e+01,8.020838322117525422e+03],
        [-1.150209535194062482e+02,8.065184953519406008e+03],
        [-1.064694837456772802e+02,8.110291483745677397e+03],
        [-1.190428718925368230e+02,8.156580871892536379e+03],
        [-1.353635336292991269e+02,8.204409533629299403e+03],
        [-9.644348283027102298e+01,8.254059482830271008e+03],
        [-6.143413116116607853e+01,8.305728131161165948e+03],
        [-3.019161311097923317e+01,8.359552613110980019e+03],
        [1.384333163552582846e+00,8.415631666836447039e+03],
        [-4.156016073666614830e+01,8.474045160736666730e+03],
        [-4.843882841860977351e+01,8.534873828418609264e+03],
        [-6.706442838867042155e+01,8.598172428388670596e+03],
        [-2.019644488579979225e+01,8.663965444885800025e+03],
        [-4.316446881084630149e+00,8.732235446881084499e+03],
        [4.435061943264736328e+01,8.802952380567352520e+03],
        [2.820550564155564643e+01,8.876083494358445023e+03],
        [5.155624419490777655e+01,8.951623755805092514e+03],
        [-4.318760899315748247e+00,9.029585760899315574e+03],
        [-6.534632828542271454e+01,9.110014328285422380e+03],
        [-7.226757738268497633e+01,9.192951577382684263e+03],
        [-9.412378615444868046e+01,9.278398786154448317e+03],
        [-1.191240653288368776e+02,9.366312065328836979e+03],
        [-4.953669826751865912e+01,9.456588698267518339e+03],
        [-6.017251579067487910e+01,9.549051515790675694e+03],
        [-5.103438828313483100e+01,9.643492388283135369e+03],
        [-7.343057830678117170e+01,9.739665578306781754e+03],
        [-2.774245193054957781e+01,9.837293451930549054e+03],
        [-3.380481112519191811e+00,9.936052481112519672e+03],
        [-2.672779877794346248e+01,1.003560179877794326e+04],
        [-3.217342505148371856e+01,1.013559842505148299e+04],
        [-4.140567518359966925e+01,1.023568267518359971e+04],
        [-6.687756033938057953e+00,1.033547475603393832e+04],
        [7.300600408459467872e+01,1.043456899591540605e+04],
        [6.862345670680042531e+01,1.053255554329319966e+04],
        [5.497882461487461114e+01,1.062907017538512628e+04],
        [9.612244093055960548e+01,1.072379155906944106e+04],
        [1.978212770103891671e+02,1.081643272298961165e+04],
        [1.362772276848754700e+02,1.090676677231512440e+04],
        [2.637635494867263333e+02,1.099469045051327339e+04],
        [1.876813256815166824e+02,1.108018567431848351e+04],
        [1.711447873158413131e+02,1.116339921268415856e+04],
        [5.257586460826678376e+01,1.124459513539173349e+04],
        [4.710652228531762375e+01,1.132414447771468258e+04],
        [-6.237613484241046535e+01,1.140245113484241119e+04],
        [-9.982044354035315337e+01,1.147994844354035376e+04],
        [-7.916275548997509759e+01,1.155703075548997549e+04],
        [-9.526003459472303803e+01,1.163403003459472347e+04],
        [-1.147987680369169539e+02,1.171122876803691724e+04],
        [-1.900259054765901965e+02,1.178884990547659072e+04],
        [-2.212256473439556430e+02,1.186704464734395515e+04],
        [-2.071394278781845060e+02,1.194584542787818464e+04],
        [-8.968541528904825100e+01,1.202514641528904758e+04],
        [-6.189531564415665343e+01,1.210471231564415575e+04],
        [-5.662878162551714922e+01,1.218425178162551674e+04],
        [-4.961678134413705266e+01,1.226343478134413635e+04],
        [-3.836288992144181975e+01,1.234189588992144127e+04],
        [-8.956671991456460091e+00,1.241923867199145570e+04],
        [3.907028461866866564e+01,1.249504271538133071e+04],
        [1.865299000184495526e+01,1.256888200999815490e+04],
        [4.279803532226833340e+01,1.264035496467773191e+04],
        [3.962735362631610769e+01,1.270907164637368442e+04],
        [1.412691291877854383e+02,1.277466887081221466e+04],
        [1.256537791844366438e+02,1.283680822081556289e+04],
        [7.067642758858892194e+01,1.289523957241141034e+04],
        [1.108876647603192396e+02,1.294979133523968085e+04],
        [9.956490829291760747e+01,1.300033609170708223e+04],
        [1.571612709880937473e+02,1.304681572901190702e+04],
        [2.318746375812715996e+02,1.308923436241872878e+04],
        [2.635546670125277160e+02,1.312769433298747208e+04],
        [2.044220965739259555e+02,1.316244290342607383e+04],
        [2.213739418903714977e+02,1.319389205810962812e+04],
        [1.020184547767112235e+02,1.322258154522328914e+04],
        [-1.072694716663390864e+02,1.324918947166633916e+04],
        [-3.490477058718843182e+02,1.327445770587188417e+04],
        [-3.975570728533530200e+02,1.329906107285335383e+04],
        [-3.331152428080622485e+02,1.332345624280806260e+04]])
    dta = macrodata.load().data['realgdp']
    res = column_stack((hpfilter(dta,1600)))
    assert_almost_equal(res,hpfilt_res,6)

def test_cfitz_filter():
    """
    Test Christiano-Fitzgerald Filter. Results taken from R.
    """
    #NOTE: The Stata mata code and the matlab code it's based on are wrong.
    cfilt_res = array([[0.712599537179426,0.439563468233128],
                        [1.06824041304411,0.352886666575907],
                        [1.19422467791128,0.257297004260607],
                        [0.970845473140327,0.114504692143872],
                        [0.467026976628563,-0.070734782329146],
                        [-0.089153511514031,-0.238609685132605],
                        [-0.452339254128573,-0.32376584042956],
                        [-0.513231214461187,-0.314288554228112],
                        [-0.352372578720063,-0.258815055101336],
                        [-0.160282602521333,-0.215076844089567],
                        [-0.0918782593827686,-0.194120745417214],
                        [-0.168083823205437,-0.158327420072693],
                        [-0.291595204965808,-0.0742727139742986],
                        [-0.348638756841307,0.037008291163602],
                        [-0.304328040874631,0.108196527328748],
                        [-0.215933150969686,0.0869231107437175],
                        [-0.165632621390694,-0.0130556619786275],
                        [-0.182326839507151,-0.126570926191824],
                        [-0.223737786804725,-0.205535321806185],
                        [-0.228939291453403,-0.269110078201836],
                        [-0.185518327227038,-0.375976507132174],
                        [-0.143900152461529,-0.53760115656157],
                        [-0.162749541550174,-0.660065018626038],
                        [-0.236263634756884,-0.588542352053736],
                        [-0.275785854309211,-0.236867929421996],
                        [-0.173666515108109,0.303436335579219],
                        [0.0963135720251639,0.779772338801993],
                        [0.427070069032285,0.929108075350647],
                        [0.629034743259998,0.658330841002647],
                        [0.557941248993624,0.118500049361018],
                        [0.227866624051603,-0.385048321099911],
                        [-0.179878859883227,-0.582223992561493],
                        [-0.428263000051965,-0.394053702908091],
                        [-0.381640684645912,0.0445437406977307],
                        [-0.0942745548364887,0.493997792757968],
                        [0.238132391504895,0.764519811304315],
                        [0.431293754256291,0.814755206427316],
                        [0.455010435813661,0.745567043101108],
                        [0.452800768971269,0.709401694610443],
                        [0.615754619329312,0.798293251119636],
                        [1.00256335412457,0.975856845059388],
                        [1.44841039351691,1.09097252730799],
                        [1.64651971120370,0.967823457118036],
                        [1.35534532901802,0.522397724737059],
                        [0.580492790312048,-0.16941343361609],
                        [-0.410746188031773,-0.90760401289056],
                        [-1.26148406066881,-1.49592867122591],
                        [-1.75784179124566,-1.87404167409849],
                        [-1.94478553960064,-2.14586210891112],
                        [-2.03751202708559,-2.465855239868],
                        [-2.20376059354166,-2.86294187189049],
                        [-2.39722338315852,-3.15004697654831],
                        [-2.38032366161537,-3.01390466643222],
                        [-1.91798022532025,-2.23395210271226],
                        [-0.982318490353716,-0.861346053067472],
                        [0.199047030343412,0.790266582335616],
                        [1.28582776574786,2.33731327460104],
                        [2.03565905376430,3.54085486821911],
                        [2.41201557412526,4.36519456268955],
                        [2.52011070482927,4.84810517685452],
                        [2.45618479815452,4.92906708807477],
                        [2.22272146945388,4.42591058990048],
                        [1.78307567169034,3.20962906108388],
                        [1.18234431860844,1.42568060336985],
                        [0.590069172333348,-0.461896808688991],
                        [0.19662302949837,-1.89020992539465],
                        [0.048307034171166,-2.53490571941987],
                        [-0.0141956981899000,-2.50020338531674],
                        [-0.230505187108187,-2.20625973569823],
                        [-0.700947410386801,-2.06643697511048],
                        [-1.27085123163060,-2.21536883679783],
                        [-1.64082547897928,-2.49016921117735],
                        [-1.62286182971254,-2.63948740221362],
                        [-1.31609762181362,-2.54685250637904],
                        [-1.03085567704873,-2.27157435428923],
                        [-1.01100120380112,-1.90404507430561],
                        [-1.19823958399826,-1.4123209792214],
                        [-1.26398933608383,-0.654000086153317],
                        [-0.904710628949692,0.447960016248203],
                        [-0.151340093679588,1.73970411237156],
                        [0.592926881165989,2.85741581650685],
                        [0.851660587507523,3.4410446351716],
                        [0.480324393352127,3.36870271362297],
                        [-0.165153230782417,2.82003806696544],
                        [-0.459235919375844,2.12858991660866],
                        [0.0271158842479935,1.55840980891556],
                        [1.18759188180671,1.17980298478623],
                        [2.43238266962309,0.904011534980672],
                        [3.08277213720132,0.595286911949837],
                        [2.79953663720953,0.148014782859571],
                        [1.73694442845833,-0.496297332023011],
                        [0.357638079951977,-1.33108149877570],
                        [-0.891418825216945,-2.22650083183366],
                        [-1.77646467793627,-2.89359299718574],
                        [-2.24614790863088,-2.97921619243347],
                        [-2.29048879096607,-2.30003092779280],
                        [-1.87929656465888,-1.05298381273274],
                        [-1.04510101454788,0.215837488618531],
                        [0.00413338508394524,0.937866257924888],
                        [0.906870625251025,0.92664365343019],
                        [1.33869057593416,0.518564571494679],
                        [1.22659678454440,0.288096869652890],
                        [0.79380139656044,0.541053084632774],
                        [0.38029431865832,1.01905199983437],
                        [0.183929413600038,1.10529586616777],
                        [0.140045425897033,0.393618564826736],
                        [0.0337313182352219,-0.86431819007665],
                        [-0.269208622829813,-1.85638085246792],
                        [-0.687276639992166,-1.82275359004533],
                        [-1.00161592325614,-0.692695765071617],
                        [-1.06320089194036,0.803577361347341],
                        [-0.927152307196776,1.67366338751788],
                        [-0.786802101366614,1.42564362251793],
                        [-0.772970884572502,0.426446388877964],
                        [-0.81275662801789,-0.437721213831647],
                        [-0.686831250382476,-0.504255468075149],
                        [-0.237936463020255,0.148656301898438],
                        [0.459631879129522,0.832925905720478],
                        [1.12717379822508,0.889455302576383],
                        [1.48640453200855,0.268042676202216],
                        [1.46515245776211,-0.446505038539178],
                        [1.22993484959115,-0.563868578181134],
                        [1.0272100765927,0.0996849952196907],
                        [0.979191212438404,1.05053652824665],
                        [1.00733490030391,1.51658415000556],
                        [0.932192535457706,1.06262774912638],
                        [0.643374300839414,-0.0865180803476065],
                        [0.186885168954461,-1.24799408923277],
                        [-0.290842337365465,-1.80035611156538],
                        [-0.669446735516495,-1.58847333561510],
                        [-0.928915624595538,-0.932116966867929],
                        [-1.11758635926997,-0.307879396807850],
                        [-1.26832454569756,-0.00856199983957032],
                        [-1.35755577149251,-0.0303537516690989],
                        [-1.34244112665546,-0.196807620887435],
                        [-1.22227976023299,-0.342062643495923],
                        [-1.04601473486818,-0.390474392372016],
                        [-0.85158508717846,-0.322164402093596],
                        [-0.605033439160543,-0.126930141915954],
                        [-0.218304303942818,0.179551077808122],
                        [0.352173017779006,0.512327303000081],
                        [1.01389600097229,0.733397490572755],
                        [1.55149778750607,0.748740387440165],
                        [1.75499674757591,0.601759717901009],
                        [1.56636057468633,0.457705308377562],
                        [1.12239792537274,0.470849913286519],
                        [0.655802600286141,0.646142040378738],
                        [0.335285115340180,0.824103600255079],
                        [0.173454596506888,0.808068498175582],
                        [0.0666753011315252,0.521488214487996],
                        [-0.0842367474816212,0.0583493276173476],
                        [-0.285604762631464,-0.405958418332253],
                        [-0.465735422869919,-0.747800086512926],
                        [-0.563586691231348,-0.94982272350799],
                        [-0.598110322024572,-1.04736894794361],
                        [-0.65216025756061,-1.04858365218822],
                        [-0.789663117801624,-0.924145633093637],
                        [-0.984704045337959,-0.670740724179446],
                        [-1.12449565589348,-0.359476803003931],
                        [-1.07878318723543,-0.092290938944355],
                        [-0.775555435407062,0.102132527529259],
                        [-0.231610677329856,0.314409560305622],
                        [0.463192794235131,0.663523546243286],
                        [1.17416973448423,1.13156902460931],
                        [1.74112278814906,1.48967153067024],
                        [2.00320855757084,1.42571085941843],
                        [1.8529912317336,0.802460519079555],
                        [1.30747261947211,-0.169219078629572],
                        [0.540237070403222,-1.01621539672694],
                        [-0.177136817092375,-1.3130784867977],
                        [-0.611981468823591,-0.982477824460773],
                        [-0.700240028737747,-0.344919609255406],
                        [-0.572396497740112,0.125083535035390],
                        [-0.450934466600975,0.142553112732280],
                        [-0.494020014254326,-0.211429053871656],
                        [-0.701707589094918,-0.599602868825992],
                        [-0.94721339346157,-0.710669870591623],
                        [-1.09297139748946,-0.47846194092245],
                        [-1.08850658866583,-0.082258450179988],
                        [-0.976082880696692,0.235758921309309],
                        [-0.81885695346771,0.365298185204303],
                        [-0.63165529525553,0.384725179378064],
                        [-0.37983149226421,0.460240196164378],
                        [-0.0375551354277652,0.68580913832794],
                        [0.361996927427804,0.984470835955107],
                        [0.739920615366072,1.13195975020298],
                        [1.03583478061534,0.88812510421667],
                        [1.25614938962160,0.172561520611839],
                        [1.45295030231799,-0.804979390544485],
                        [1.64887158748426,-1.55662011197859],
                        [1.78022721495313,-1.52921975346218],
                        [1.71945683859668,-0.462240366424548],
                        [1.36728880239190,1.31213774341268],
                        [0.740173894315912,2.88362740582926],
                        [-0.0205364331835904,3.20319080963167],
                        [-0.725643970956428,1.75222466531151],
                        [-1.23900506689782,-0.998432917440275],
                        [-1.52651897508678,-3.72752870885448],
                        [-1.62857516631435,-5.00551707196292],
                        [-1.59657420180451,-4.18499132634584],
                        [-1.45489013276495,-1.81759097305637],
                        [-1.21309542313047,0.722029457352468]])
    dta = macrodata.load().data[['tbilrate','infl']].view((float,2))[1:]
    cyc, trend = cffilter(dta)
    assert_almost_equal(cyc, cfilt_res, 8)
    #do 1d
    cyc, trend = cffilter(dta[:,1])
    assert_almost_equal(cyc, cfilt_res[:,1], 8)

def test_bking_pandas():
    # 1d
    dta = macrodata.load_pandas().data
    index = Index(dates_from_range('1959Q1', '2009Q3'))
    dta.index = index
    filtered = bkfilter(dta["infl"])
    nd_filtered = bkfilter(dta['infl'].values)
    assert_equal(filtered.values, nd_filtered)
    assert_equal(filtered.index[0], datetime(1962, 3, 31))
    assert_equal(filtered.index[-1], datetime(2006, 9, 30))
    assert_equal(filtered.name, "infl")

    #2d
    filtered = bkfilter(dta[["infl","unemp"]])
    nd_filtered = bkfilter(dta[['infl', 'unemp']].values)
    assert_equal(filtered.values, nd_filtered)
    assert_equal(filtered.index[0], datetime(1962, 3, 31))
    assert_equal(filtered.index[-1], datetime(2006, 9, 30))
    assert_equal(filtered.columns.values, ["infl", "unemp"])

def test_cfitz_pandas():
    # 1d
    dta = macrodata.load_pandas().data
    index = Index(dates_from_range('1959Q1', '2009Q3'))
    dta.index = index
    cycle, trend = cffilter(dta["infl"])
    ndcycle, ndtrend = cffilter(dta['infl'].values)
    assert_equal(cycle.values, ndcycle)
    assert_equal(cycle.index[0], datetime(1959, 3, 31))
    assert_equal(cycle.index[-1], datetime(2009, 9, 30))
    assert_equal(cycle.name, "infl")

    #2d
    cycle, trend = cffilter(dta[["infl","unemp"]])
    ndcycle, ndtrend = cffilter(dta[['infl', 'unemp']].values)
    assert_equal(cycle.values, ndcycle)
    assert_equal(cycle.index[0], datetime(1959, 3, 31))
    assert_equal(cycle.index[-1], datetime(2009, 9, 30))
    assert_equal(cycle.columns.values, ["infl", "unemp"])

def test_hpfilter_pandas():
    dta = macrodata.load_pandas().data
    index = Index(dates_from_range('1959Q1', '2009Q3'))
    dta.index = index
    cycle, trend = hpfilter(dta["realgdp"])
    ndcycle, ndtrend = hpfilter(dta['realgdp'].values)
    assert_equal(cycle.values, ndcycle)
    assert_equal(cycle.index[0], datetime(1959, 3, 31))
    assert_equal(cycle.index[-1], datetime(2009, 9, 30))
    assert_equal(cycle.name, "realgdp")

if __name__ == "__main__":
    import nose
    nose.runmodule(argv=[__file__, '-vvs', '-x', '--pdb'], exit=False)
