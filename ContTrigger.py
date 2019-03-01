function keepMyServerAlive() {
  
  var allMySites = ['https://saurav-scholar.rounak.repl.co/'];
  
  for (var siteIndex in allMySites) {
    var currentSite = allMySites[siteIndex];
    
    try {
      var response = UrlFetchApp.fetch(currentSite);
      Logger.log(response.getContentText());
    } catch(e) {
      Logger.log(e);
    }
    
  }  
  
}
