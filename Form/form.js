$(document).ready(function() {
  $("#phone-number").intlTelInput({
    preferredCountries: ['us', 'gb', 'jp', 'cn'],
    defaultCountry: 'us'
  });
});

$(document).ready(function() {
  var countryList = window.intlTelInputGlobals.getCountryData();
  for (var i = 0; i < countryList.length; i++) {
    var country = countryList[i];
    $('#country-selector').append('<option>' + country.name + '</option>');
  }
});

