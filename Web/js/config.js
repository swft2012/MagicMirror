// for navigator language
//var lang = window.navigator.language;
var lang = 'kr';
// you can change the language
// var lang = 'en';

//change weather params here:
//units: metric or imperial
var weatherParams = {
    'q':'Cheongju,KR',
    'units':'metric',
    'lang':lang
};

var feed = 'http://feeds2.feedburner.com/normalog';
//var feed = 'http://feeds.feedburner.com/channy';
//var feed = 'http://feeds.nos.nl/nosjournaal?format=rss';
//var feed = 'http://www.nu.nl/feeds/rss/achterklap.rss';
//var feed = 'http://www.nu.nl/feeds/rss/opmerkelijk.rss';
//var feed = 'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml';

// compliments:
var morning = [
            '좋은아침:-)',
            '오늘 하루도 힘내세요!',
            '잘잤나요?'
        ];
        
var afternoon = [
            '안녕 예쁜이!',
            '멋져보이네요!',
            '좋은 하루인 것 같네요!'
        ];
       
var evening = [
            '저녁 먹었어요?',
            '오늘 고생했어요!',
            '잘 자요!'
            //'Wow, you look hot!',
            //'You look nice!',
            //'Hi, sexy!'
        ];