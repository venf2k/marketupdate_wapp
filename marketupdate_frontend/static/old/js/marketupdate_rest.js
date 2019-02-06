// create REST endpoint for images
myApp.factory('Updates', function($resource) {
  return $resource('/api/updates/');
});