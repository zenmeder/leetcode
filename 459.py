#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(2, length+1)[::-1]:
            if length % i:
                continue
            lp = length//i
            if s==s[:lp] * i:
                return True
        return False
print(Solution().repeatedSubstringPattern('rstvvqxwwytlhtmddecbeluloucjbnjrltxkwykjehlpnioghuarrnitpgbxkjvenuphpmpszyospiyeitiyodcpnynckdqxozqmgghogviwkauvzwjvuihndwnrlloucyqtppcrdhhotkymwamdqldmtnldlggfbfoojtsijkojrshbsmsmgtbjmggdfcfdekinrctgnuflwczcefledrknbwmsaduuqmlcbnzqkfvvghyspeujnguhillguzbfoshebuydkpsojvxcuirihjidvjkjnedhgmdlxbabnlbdtacanykejyahlkkifyjrqrdootrbjomjbgglunxilrahojxughookuhtbktanideubykfldptffrqazpqouexopcjwskakvpjfsjfkwdptdxerdgbkvjemfmpnologehchcwjqfwqmrodnsavyqyjulkedicuwwkuqtflpykmdxomrfwavtsehwqfutezytvuyxeyioljqmkkyyvnaltuhskpcsrxemjwlqauqppofkkhrwjjxyikqvllqjcuwlkxyvvomkbclxnfufnxwephybchgmcnlcnjhqlfcinuikqzeeiupmcxbhsxkhooxgzyjppkdnqonfcjgvywdduxtitbvbrzuaqkvgkeukhnxdpniyrofwbcvszwrhdsjnjxdgmozyjmmqesmkmpqkachcczlsmvudxnevhprzvurwrjkwchweosteewlufwplswtcovjbglmataxbgxolcjkrmuhrshrxtppawguptnnkchcsdorotbrixvdhzuyqyquyllijrnqdyppasqogtejplkosjuyoxmpnmeciykzwhafecdthfzqptjqleagydeixkzuceniluoarzxmdbipvqhrgukiyqpgkaqrxkyyrixhpiijqlmylikaxprqbbbrrnaldymccagmmskisbgnxqbvqvdnpaonwavamtwhcumpdlawgbrirzggddhciauwvvvesuqokuusjolfilheeerunywbewyvooayegiscyrcjutxkyovrztmeiwkbwmxvgzkcpniwtdmtmnzhzxnqnaterhyhajnzddnhktvfgfxjfzwlspmkbpexsycykwhycufivauovumdnkmznbjkocinyjqocxcerxsuacozbvckflnhwpitiypbnykcwuvrpbpdktpztmvaqqqpyxtayouyyngzyszorrynhzcxkarmewxbjzkzsuwsfguwubbffcasxozaqzjiijsvnkkbgmfrocfmkxypefvkxnfhdoqrxmibqlrcnnkbkyghxdkbxabtefhxithrbhlyjnthvbztadudjkpxpdknpudwltdhjtugzujnewmkxdyocwmhndebvoiderilgmtdwchrfihrmmztglrvtuyhqenpbnandznjevgqsuufcdcnzbwohrfapfodnqrnlkkkmuthbjkiddbcyrtqolaxozopxwapvwdnzoqxfjczsfgsiosahqsnfzbdkihdtytvrrrmvlymywcbrvssqpbqbotvaqpqywebiyymzlpguemcgwldxjrtgegobaocfqibinyuneoyzyghexdhnjklaabaseelxetappktcidpvigmeyfdugceaviyptgrqfktwhlaholatcnrwkdkpcsddxtfsqbchnbazlvorzsmfflooecqcyonqdkcoxdmwtdkzfwhnpexrlykytramordfiecgmyxmdrmaalvseklmtbnfcrbhcmgaluxdvmyhflxatcgjejclgsptscqgdemouqisubthcluerdhxhekelvenigatnzefhbavmwajegzqxmmdhgmlmnndbnqhicrrwtgljgirobgexpmzkaklgryrkueolokwaazfxbfbyrurzzojuoeliexgwvxcwrjvyisvvzsvsthaoarrgykkrezkknlxgcprfruhxkafxlfepleqvpfptheypdqelfjteqvtpmxnuyvxqmjprcieqidceeqdpzylpuisewzpwujyetvavgvsyknglxdhmrnnuxfgmqzgheljmugsdrbreckdynrmuegyurtnwhplcziosbjegdaygtshhhibqsjgfywnigbdjruqfktbhpptocpaoqdmzeluqptljcyjnibwtqpkhwvqgiwgrbdfqaxumjkdmvrrhpvbyuwodctkzoxqegosuauqwssouhejzqyeaidtshdcifdngnxzejshsdojfxxmwioqqctcchdqtnmbacoqtjxiaymkxbznwezpsoonlluqawvezoekiwymibqudloejfoqvygcoqaokoqzopyqnyywuntvcvxagbktwwmkfkkvguyepmxkvujczbaooskewkvxykdeidnemgnbhypxpzgkifgxlxkttrlpyjnedsbhdkeurzefnrtikmrglctmlrgubxsrqfswbyeiwueymhqoxnnmgjvqfdramurslxfokenqlxfkmbbuyiwlyuczssxidjedkrrtbjnjjovykqyosvjzaxhqtnzrpyxtzpudmlklwvvvamqdrjonmtrkaghrirwytupnbpvfgvuecujtbsrlndafiqzijiqjkrhuqluvzfiibdydrzjmtqhygqwsgjhhwnubkbqpgmzdbtiuipwhpvpcmjfnvbftfvlryzphvgxkvzdalznizsbrnlllwbezeqxrrkjfvbqhhqymwykacrxqvezkktxaftypzqthkplgrqbrqdlcmnvyhwuecsbovrneuzxmtpfrcxbjozpoqneifyrkvrrrgcgnniwvatsincxnxikcfpghhrtgqyldbgvzjwfxgdrqhkbyhbcmxpkayhcpxgrjhtpmvtztwizkuwdyafphdujphgsikzfcnsddwldyzoefiunwcndijukmgqhmfusykdprprxjmsrqkkroiyuziaxxvmrpjnvycfmprxkeghhtzlrbznwjsjvmhifbmxomlleuqkmydilxkisgktfjgxmeskqdqapszefjaxmzswovzmrnxnrmklmzkgiijywfitfjqaunpwfiimwnwpergctopcbyuwqivtmoyzqdhwlmqpxajchmzlyipavbkjjrtuarwllkhnubhdmomtxpzhpjdktonjzivmadfgkipgqmqaclttvqmxdoqbtcrcwbktrudhgzrkbgvzfzurwhenisrsghiltsblblmmrjeyixsrowtqotbllbwngtfvcffkpbxanmnmgbzqbdawdytgmsaqnldkrjrdcvdefxhhwvjikevbxoxmfrisghtppxmaisyesluodaqnuvzhiyjhfgtdspzzqbxzikhflmqkojbbapugbrkinslotdmfirjgeblyrvfufckzjrkwnfrveytccjpwvktixalpekygtunleysakzbcaakjsgbszuqeoidqqeypfcqlkbxtkpromxcpzavqvhkcgrnzldjqxvtilennmgwbvmezvbacvdjeahzhdslnqtejtsncdshjxrwaldmwggdmefgshazrfuvrpilvadzznatldrxxhsnztvvqdifjlufeacighttujqygltotlupvgxbtdiljfaprvxytkrdlktjfbceyrkvyqnbmssaucoovrssmnzboqmvpdqsionefmughyjlyuupjyiklsprjzgcdykmxncszrldjytrblntzvdrqzfygdwetkjzmppeyjluvclcdixqjuyjhrqqpqhuwzmpikpfkevrxvybjpnwzbgfwlplafbslhjwlvommelhwbzibqgcdcmnbnhnttroecgysjvbwizfhjmzyddgztzpydchhxbfcdukhrtfnjlynqpbhprwmontrjdloxdfzlnqbfmvglrhmaohjgvalxlxjjvzsuifyffxpsijfaovkmeabtkpxnixplnakjohobcnefuowlvmiwhdfabienqkjgzpaujazcyfnhrtbtsbyhnocemhtknzizzootmmkljrxhdpvbsynasamkamyjiryreysoxgognbqlvwldnyheaocxwmtnpdsekajfezbjujluigkofjmdkgjybcsqszvbvnyymtkqdufitvewanelrtxzuefunpenjmquikxlpcrtzscautvqmsevvkcwqyzdvzkomfahqcdgmthfrrjxmfuyonajvzmwwqtfcvhqranfsjbgqjvwvejbjlljenetqredxczrcshkuokhlruidkontvlrpwuxmmrgfigecbccqmnllrjhebikreubnotpjskfwjrtjeoqzrzwmobqgeryydlpqvymfvskeelyaiwcfkizgemqkvgsicuekzdjjxuspjthhyulwkrflcuimmmcmzgeghteagnhbbgrjsgboymcwusiphafwznxhtrpoblnukrhjsdvzqtalfhqwcnzvbmobzrivqjwuifktpfdchuyipllcmjoyemscundxakhconhibakifrrobrwlwnohgitbmdqyqunviwcadwczrkgbtafpjeltxpgxknsmmxpkzynjejhwqwiqgwaezryhpqgqqfeovjgnzhaaezabhnszorllrstvvqxwwytlhtmddecbeluloucjbnjrltxkwykjehlpnioghuarrnitpgbxkjvenuphpmpszyospiyeitiyodcpnynckdqxozqmgghogviwkauvzwjvuihndwnrlloucyqtppcrdhhotkymwamdqldmtnldlggfbfoojtsijkojrshbsmsmgtbjmggdfcfdekinrctgnuflwczcefledrknbwmsaduuqmlcbnzqkfvvghyspeujnguhillguzbfoshebuydkpsojvxcuirihjidvjkjnedhgmdlxbabnlbdtacanykejyahlkkifyjrqrdootrbjomjbgglunxilrahojxughookuhtbktanideubykfldptffrqazpqouexopcjwskakvpjfsjfkwdptdxerdgbkvjemfmpnologehchcwjqfwqmrodnsavyqyjulkedicuwwkuqtflpykmdxomrfwavtsehwqfutezytvuyxeyioljqmkkyyvnaltuhskpcsrxemjwlqauqppofkkhrwjjxyikqvllqjcuwlkxyvvomkbclxnfufnxwephybchgmcnlcnjhqlfcinuikqzeeiupmcxbhsxkhooxgzyjppkdnqonfcjgvywdduxtitbvbrzuaqkvgkeukhnxdpniyrofwbcvszwrhdsjnjxdgmozyjmmqesmkmpqkachcczlsmvudxnevhprzvurwrjkwchweosteewlufwplswtcovjbglmataxbgxolcjkrmuhrshrxtppawguptnnkchcsdorotbrixvdhzuyqyquyllijrnqdyppasqogtejplkosjuyoxmpnmeciykzwhafecdthfzqptjqleagydeixkzuceniluoarzxmdbipvqhrgukiyqpgkaqrxkyyrixhpiijqlmylikaxprqbbbrrnaldymccagmmskisbgnxqbvqvdnpaonwavamtwhcumpdlawgbrirzggddhciauwvvvesuqokuusjolfilheeerunywbewyvooayegiscyrcjutxkyovrztmeiwkbwmxvgzkcpniwtdmtmnzhzxnqnaterhyhajnzddnhktvfgfxjfzwlspmkbpexsycykwhycufivauovumdnkmznbjkocinyjqocxcerxsuacozbvckflnhwpitiypbnykcwuvrpbpdktpztmvaqqqpyxtayouyyngzyszorrynhzcxkarmewxbjzkzsuwsfguwubbffcasxozaqzjiijsvnkkbgmfrocfmkxypefvkxnfhdoqrxmibqlrcnnkbkyghxdkbxabtefhxithrbhlyjnthvbztadudjkpxpdknpudwltdhjtugzujnewmkxdyocwmhndebvoiderilgmtdwchrfihrmmztglrvtuyhqenpbnandznjevgqsuufcdcnzbwohrfapfodnqrnlkkkmuthbjkiddbcyrtqolaxozopxwapvwdnzoqxfjczsfgsiosahqsnfzbdkihdtytvrrrmvlymywcbrvssqpbqbotvaqpqywebiyymzlpguemcgwldxjrtgegobaocfqibinyuneoyzyghexdhnjklaabaseelxetappktcidpvigmeyfdugceaviyptgrqfktwhlaholatcnrwkdkpcsddxtfsqbchnbazlvorzsmfflooecqcyonqdkcoxdmwtdkzfwhnpexrlykytramordfiecgmyxmdrmaalvseklmtbnfcrbhcmgaluxdvmyhflxatcgjejclgsptscqgdemouqisubthcluerdhxhekelvenigatnzefhbavmwajegzqxmmdhgmlmnndbnqhicrrwtgljgirobgexpmzkaklgryrkueolokwaazfxbfbyrurzzojuoeliexgwvxcwrjvyisvvzsvsthaoarrgykkrezkknlxgcprfruhxkafxlfepleqvpfptheypdqelfjteqvtpmxnuyvxqmjprcieqidceeqdpzylpuisewzpwujyetvavgvsyknglxdhmrnnuxfgmqzgheljmugsdrbreckdynrmuegyurtnwhplcziosbjegdaygtshhhibqsjgfywnigbdjruqfktbhpptocpaoqdmzeluqptljcyjnibwtqpkhwvqgiwgrbdfqaxumjkdmvrrhpvbyuwodctkzoxqegosuauqwssouhejzqyeaidtshdcifdngnxzejshsdojfxxmwioqqctcchdqtnmbacoqtjxiaymkxbznwezpsoonlluqawvezoekiwymibqudloejfoqvygcoqaokoqzopyqnyywuntvcvxagbktwwmkfkkvguyepmxkvujczbaooskewkvxykdeidnemgnbhypxpzgkifgxlxkttrlpyjnedsbhdkeurzefnrtikmrglctmlrgubxsrqfswbyeiwueymhqoxnnmgjvqfdramurslxfokenqlxfkmbbuyiwlyuczssxidjedkrrtbjnjjovykqyosvjzaxhqtnzrpyxtzpudmlklwvvvamqdrjonmtrkaghrirwytupnbpvfgvuecujtbsrlndafiqzijiqjkrhuqluvzfiibdydrzjmtqhygqwsgjhhwnubkbqpgmzdbtiuipwhpvpcmjfnvbftfvlryzphvgxkvzdalznizsbrnlllwbezeqxrrkjfvbqhhqymwykacrxqvezkktxaftypzqthkplgrqbrqdlcmnvyhwuecsbovrneuzxmtpfrcxbjozpoqneifyrkvrrrgcgnniwvatsincxnxikcfpghhrtgqyldbgvzjwfxgdrqhkbyhbcmxpkayhcpxgrjhtpmvtztwizkuwdyafphdujphgsikzfcnsddwldyzoefiunwcndijukmgqhmfusykdprprxjmsrqkkroiyuziaxxvmrpjnvycfmprxkeghhtzlrbznwjsjvmhifbmxomlleuqkmydilxkisgktfjgxmeskqdqapszefjaxmzswovzmrnxnrmklmzkgiijywfitfjqaunpwfiimwnwpergctopcbyuwqivtmoyzqdhwlmqpxajchmzlyipavbkjjrtuarwllkhnubhdmomtxpzhpjdktonjzivmadfgkipgqmqaclttvqmxdoqbtcrcwbktrudhgzrkbgvzfzurwhenisrsghiltsblblmmrjeyixsrowtqotbllbwngtfvcffkpbxanmnmgbzqbdawdytgmsaqnldkrjrdcvdefxhhwvjikevbxoxmfrisghtppxmaisyesluodaqnuvzhiyjhfgtdspzzqbxzikhflmqkojbbapugbrkinslotdmfirjgeblyrvfufckzjrkwnfrveytccjpwvktixalpekygtunleysakzbcaakjsgbszuqeoidqqeypfcqlkbxtkpromxcpzavqvhkcgrnzldjqxvtilennmgwbvmezvbacvdjeahzhdslnqtejtsncdshjxrwaldmwggdmefgshazrfuvrpilvadzznatldrxxhsnztvvqdifjlufeacighttujqygltotlupvgxbtdiljfaprvxytkrdlktjfbceyrkvyqnbmssaucoovrssmnzboqmvpdqsionefmughyjlyuupjyiklsprjzgcdykmxncszrldjytrblntzvdrqzfygdwetkjzmppeyjluvclcdixqjuyjhrqqpqhuwzmpikpfkevrxvybjpnwzbgfwlplafbslhjwlvommelhwbzibqgcdcmnbnhnttroecgysjvbwizfhjmzyddgztzpydchhxbfcdukhrtfnjlynqpbhprwmontrjdloxdfzlnqbfmvglrhmaohjgvalxlxjjvzsuifyffxpsijfaovkmeabtkpxnixplnakjohobcnefuowlvmiwhdfabienqkjgzpaujazcyfnhrtbtsbyhnocemhtknzizzootmmkljrxhdpvbsynasamkamyjiryreysoxgognbqlvwldnyheaocxwmtnpdsekajfezbjujluigkofjmdkgjybcsqszvbvnyymtkqdufitvewanelrtxzuefunpenjmquikxlpcrtzscautvqmsevvkcwqyzdvzkomfahqcdgmthfrrjxmfuyonajvzmwwqtfcvhqranfsjbgqjvwvejbjlljenetqredxczrcshkuokhlruidkontvlrpwuxmmrgfigecbccqmnllrjhebikreubnotpjskfwjrtjeoqzrzwmobqgeryydlpqvymfvskeelyaiwcfkizgemqkvgsicuekzdjjxuspjthhyulwkrflcuimmmcmzgeghteagnhbbgrjsgboymcwusiphafwznxhtrpoblnukrhjsdvzqtalfhqwcnzvbmobzrivqjwuifktpfdchuyipllcmjoyemscundxakhconhibakifrrobrwlwnohgitbmdqyqunviwcadwczrkgbtafpjeltxpgxknsmmxpkzynjejhwqwiqgwaezryhpqgqqfeovjgnzhaaezabhnszorll'))