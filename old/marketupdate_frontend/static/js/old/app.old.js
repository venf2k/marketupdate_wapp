(function () {
'use strict';

angular.module('MarketUpdateApp', [])
.controller('TabsMarketUpdateController', TabsMarketUpdateController)
.service('TabsMarketUpdateService', TabsMarketUpdateService)
.constant('ApiBasePath', "http://127.0.0.1:8000/api/");
.constant('LastMarketUpdate', "last_market_update/");


TabsMarketUpdateController.$inject = ['TabsMarketUpdateService'];
function TabsMarketUpdateController(TabsMarketUpdateService) {
  var tabs = this;

  var promise = TabsMarketUpdateService.getTabsMarketUpdate();

  promise.then(function (response) {
    tabs.last_market_update_data = response.data;
  })
  .catch(function (error) {
    console.log("Something went terribly wrong.");
  });

  menu.logMenuItems = function (shortName) {
    var promise = TabsMarketUpdateService.getTabsMarketUpdate(shortName);

    promise.then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    })
  };

}


TabsMarketUpdateService.$inject = ['$http', 'ApiBasePath'];
function TabsMarketUpdateService($http, ApiBasePath) {
  var service = this;

  service.getTabsMarketUpdate = function () {
    var response = $http({
      method: "GET",
      url: (ApiBasePath + LastMarketUpdate)
    });

    return response;
  };


  service.getTabsMarketUpdate = function (shortName) {
    var response = $http({
      method: "GET",
      url: (ApiBasePath + LastMarketUpdate + shortName),
      //params: {
      //  category: shortName
      //}
    });

    return response;
  };

}

})();
