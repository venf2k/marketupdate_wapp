// create REST endpoint for images
myApp.factory('Updates', function($scope, $resource) {
  return $resource('/api/updates/:pk', {'pk': '@pk'});
});