(function () {
'use strict';

angular.module('MarketUpdateApp', [])
.controller('MarketUpdateController', MarketUpdateController)
.service('MarketUpdateService', MarketUpdateService)
.constant('ApiBasePath', "http://127.0.0.1:8000/api/")
.constant('TabsURL', "last_market_update/");

MarketUpdateController.$inject = ['MarketUpdateService'];
function MarketUpdateController(MarketUpdateService) {
  var menu = this;

  var promise = MarketUpdateService.getMarketUpdate();

  promise.then(function (response) {
    menu.MarketData = response.data;
  })
  .catch(function (error) {
    console.log("Something went terribly wrong.");
  });

  menu.logMenuItems = function (shortName) {
    var promise = MarketUpdateService.getMenuForCategory(shortName);

    promise.then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    })
  };

}


MarketUpdateService.$inject = ['$http', 'ApiBasePath', 'TabsURL'];
function MarketUpdateService($http, ApiBasePath, TabsURL) {
  var service = this;

  service.getMarketUpdate = function () {
    var response = $http({
      method: "GET",
      url: (ApiBasePath + TabsURL)
    });

    return response;
  };


  service.getMenuForCategory = function (shortName) {
    var response = $http({
      method: "GET",
      url: (ApiBasePath + TabsURL),
      params: {
        category: shortName
      }
    });

    return response;
  };

}

})();
