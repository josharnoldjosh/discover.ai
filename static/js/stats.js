$(function(){
        var ul = document.getElementById('place_list');
        
    
    for (var i = 0; i < molecules.length; i++) {
       var li = document.createElement("li");
        li.innerHTML = ('<div class="atom-loader"><div class="atom-inner atom-one"></div><div class="atom-inner atom-two"></div><div class="atom-inner atom-three"></div><div class="atom-inner atom-four"></div><div class="atom-inner atom-center-one"></div><div class="atom-inner atom-center-two"></div><div class="atom-inner atom-center-three"></div><div class="atom-inner atom-center-four"></div> </div>');
        var span = document.createElement("span");
       li.className = 'list-element'; span.appendChild(document.createTextNode(molecules[i].name + "\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0|\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0" + molecules[i].probability));
        li.appendChild(span);
        ul.appendChild(li);
    }

})

var molecules =[
    {"name":"Molecule 1", "probability":0.99},
    {"name":"Molecule 2", "probability":0.89},
    {"name":"Molecule 3", "probability":0.79},
    {"name":"Molecule 4", "probability":0.69},
    {"name":"Molecule 5", "probability":0.89},
    {"name":"Molecule 6", "probability":0.79},
    {"name":"Molecule 7", "probability":0.69},
    {"name":"Molecule 8", "probability":0.59},
    {"name":"Molecule 9", "probability":0.49},
    {"name":"Molecule 10", "probability":0.29},
    {"name":"Molecule 11", "probability":0.19},
    {"name":"Molecule 12", "probability":0.11},
    {"name":"Molecule 13", "probability":0.21},
    {"name":"Molecule 14", "probability":0.34},
    {"name":"Molecule 15", "probability":0.96},
    {"name":"Molecule 16", "probability":0.98},
    {"name":"Molecule 17", "probability":0.23},
    {"name":"Molecule 18", "probability":0.08},
    {"name":"Molecule 19", "probability":0.02}
    
];

var percentages = [
    {   "range" : "90-100", "number" : 0.0 },
    {   "range" : "80-90", "number" : 0.0 },
    {   "range" : "70-80", "number" : 0.0 },
    {   "range" : "60-70", "number" : 0.0 },
    {   "range" : "50-60", "number" : 0.0 },
    {   "range" : "40-50", "number" : 0.0 },
    {   "range" : "30-40", "number" : 0.0 },
    {   "range" : "20-30", "number" : 0.0 },
    {   "range" : "10-20", "number" : 0.0 },
    {   "range" : "00-10", "number" : 0.0 },
];

var getPercent = function(){
    for(var i = 0; i < molecules.length; i++)
    {
        if(molecules[i].probability > 0.9)
            percentages[0].number = percentages[0].number + 1;
        else if(molecules[i].probability > 0.8)
            percentages[1].number = percentages[1].number + 1;
        else if(molecules[i].probability > 0.7)
            percentages[2].number = percentages[2].number + 1;
        else if(molecules[i].probability > 0.6)
            percentages[3].number = percentages[3].number + 1;
        else if(molecules[i].probability > 0.5)
            percentages[4].number = percentages[4].number + 1;
        else if(molecules[i].probability > 0.4)
            percentages[5].number = percentages[5].number + 1;
        else if(molecules[i].probability > 0.3)
            percentages[6].number = percentages[6].number + 1;
        else if(molecules[i].probability > 0.2)
            percentages[7].number = percentages[7].number + 1;        
        else if(molecules[i].probability > 0.1)
            percentages[8].number = percentages[8].number + 1;
        else 
            percentages[9].number = percentages[9].number + 1;
    }
}
    getPercent();
        var chart = AmCharts.makeChart( "chartdiv", {
          "type": "pie",
          "theme": "none",

          "dataProvider": percentages,
          "valueField": "number",
          "titleField": "range",
           "balloon":{
           "fixedPosition":true
          },
          "export": {
            "enabled": false
          }
        } );
                






