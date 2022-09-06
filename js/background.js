chrome.contextMenus.create({
    "id":'Virustotal',
    "title": "Virustotal",
    "contexts": ["link"], 

});
chrome.contextMenus.onClicked.addListener(opentab())


function opentab(){
    return function(){
        chrome.tabs.create ({url: "https://www.virustotal.com/gui/home/url" })
    }
};
