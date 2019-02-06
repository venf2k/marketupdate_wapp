var myApp = angular.module('marketupdate_frontend', ['ngRoute', 'ngResource']);

myApp.config(function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller( 'MainCtrl', function($scope, updates) 
{
	console.log('In main Control')
	updates = Updates.query();
});	