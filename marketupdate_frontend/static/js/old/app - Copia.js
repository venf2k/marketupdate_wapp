(function () {
'use strict';

angular.module('MarketUpdateApp', [])
.controller('MarketUpdateController', MarketUpdateController)
.service('MarketUpdateService', MarketUpdateService)
.filter('unique', UniqueFilter)
.filter('RestN', RestNFilter)
.filter('PValue', PValueFilter)
.constant('ApiBasePath', "http://127.0.0.1:8000/api/");


MarketUpdateController.$inject = ['MarketUpdateService'];
function MarketUpdateController(MarketUpdateService) {
  var menu = this;

  var promise = MarketUpdateService.getMarketUpdate();

  promise.then(function (response) {
    menu.market_update_set = response.data;
  })
  .catch(function (error) {
    console.log("Something went terribly wrong.");
  });

}

MarketUpdateService.$inject = ['$http', 'ApiBasePath'];
function MarketUpdateService($http, ApiBasePath) {
  var service = this;

  service.getMarketUpdate = function () {
    var response = $http({
      method: "GET",
      url: (ApiBasePath + "last_market_update/")
    });

    return response;
  };

}

function UniqueFilter() {
  return function (collection, keyname) {
     // we define our output and keys array;
    var output = [], 
        keys = [];
      
    // we utilize angular's foreach function
    // this takes in our original collection and an iterator function
    angular.forEach(collection, function(item) {
        // we check to see whether our object exists
        var key = item[keyname];
        // if it's not already part of our keys array
        if(keys.indexOf(key) === -1) {
            // add it to our keys array
            keys.push(key); 
            // push this item to our final output array
            output.push(item);
        }
    });
    // return our array which should be devoid of
    // any duplicates
    return output;
  }
}


function RestNFilter() {
  return function (collection, N) {
     // we define our output and keys array;
    var output = [];
    for(var i=0;i< ( N - collection.length-1 );i++) {
      output.push(N);
    }
    // return our array which should be devoid of
    // any duplicates
    console.log("Debug:");
    console.log(N-collection.length-1);
    return output;
  }
}

/*   
function RestNFilter() {
  return function (collection, N) {
     // we define our output and keys array;
    var output = []; 
    var i = 1;
 
    var RestN = collection.length() - N;
      
    if(RestN > 0 ) {
        // push this item to our final output array
        for (var i = RestN - 1; i >= 0; i--) 
          output.push(i);

        }
    }
    return output;

    console.log("Debug:");
    console.log(i);
  }
}
*/

// -> Funzione non utilizzata 
function PValueFilter() {
  return function (collection, keyname, value) {
     // we define our output and keys array;
    var output = [];
      
    // we utilize angular's foreach function
    // this takes in our original collection and an iterator function
    angular.forEach(collection, function(item) {
        // we check to see whether our object exists
        var key = item[keyname];
        // if it's not already part of our keys array
        if(key === value) {
            // push this item to our final output array
            output.push(item);
        }
    });
    // return our array which should be devoid of
    // any duplicates
    console.log("Debug:");
    console.log(value);
    console.log(keyname);
    return output;
  }
}



})();
