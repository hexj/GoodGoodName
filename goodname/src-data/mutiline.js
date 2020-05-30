Function.prototype.getMultiLine = function() {
    var lines = new String(this);
    lines = lines.substring(lines.indexOf("/*") + 3, lines.lastIndexOf("*/"));
    return lines;
}

var string = function() {
    /*
锏：多才贤能，荣贵隆昌，晚婚大吉，中年劳，晚年吉祥。
镫：身瘦多才，清雅荣贵，中年吉祥，晚年隆昌，环境良好。
镪：智勇双全，义利分明，中年平凡但奔波，晚年隆昌，官运旺。
译：一生清闲量大，上下敦睦，爱人所爱，中年吉祥，晚年隆昌。
钟：一生清雅多才，克己助人，中年平凡，晚年隆昌。
藏：温和清雅，多才贤能，出外吉祥，中年劳，晚年隆昌。
籍：晚婚迟得子吉，白手成家，自力更生，中年勤俭，晚年隆昌。
舰：性刚果断，多才贤能，中年劳，晚年吉祥，环境良好。
牺：多才贤能，温和伶俐，中年平凡，晚年吉祥，环境良好，忌车怕水。
薰：衣厚食丰，秀气巧妙，清雅荣贵，官运旺，出国之字。
严：智勇双全，忠厚善良，事业如意，官运旺，成功隆昌，荣贵之字。
议：英雄格，多才贤能，白手成家，快乐自在，晚年隆昌。
迈：少年艰难，出外逢贵得财，中年劳，晚年隆昌，官运旺。
瀜：清雅多才，温和伶俐，中年劳，晚年吉祥，女人有爱情烦恼。
阐：孤独格，清雅伶俐，福禄双收，中年劳，晚年吉祥，忌车怕水。
赡：福禄双收，特有人缘，中年劳，晚年吉祥。
耀：天生聪颖，清雅荣贵，多才贤能，中年成功隆昌，出国之格。
矿：命硬，晚婚吉祥，二子吉祥，中年吉祥，环境良好。
    */
}

linesarr = string.getMultiLine().split(/\r?\n/)
var ziobj = {}

for (j = 0, len = linesarr.length; j < len; j++) {
    line = linesarr[j]
    ziobj[line.substr(0, 1)] = line
    // console.log(line.substr(0, 1))
}

function getzi(obj){
    zi = obj.value
    if (ziobj.hasOwnProperty(zi)){
        console.log(ziobj[zi])
    }
}
$x('//*[@id="tb"]/tbody/tr[9]/td/table/tbody/tr[1]/td/input').forEach(getzi)
