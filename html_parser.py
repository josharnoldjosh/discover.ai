#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 06:21:23 2018

@author: josharnold
"""

class text_parser:
    def create_html(result):        
        mol_array_str = "var molecules =["

        num_moles_to_show = len(result)
        #num_moles_to_show = len(result)
        for i in range(0, num_moles_to_show):
            if i < (num_moles_to_show-1):
                
                mol_array_str += " {\"name\":\"" + "Molecule " + str(result[i][0]) + "\", \"probability\":\"" + str(result[i][1]) + "\"},"
            else:
                mol_array_str += " {\"name\":\"" + "Molecule " + str(result[i][0]) + "\", \"probability\":\"" + str(result[i][1]) + "\"}"
        
        mol_array_str += "];"                  
            
        return text_parser.top_half() + mol_array_str + text_parser.get_bottom_half()
        
    
    def top_half():
        val = """
    
    <!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <title>Drug Maker</title>
      <meta name="description" content="Save lives! save money!">

    </head>

    <body>

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


      <script src="https://www.amcharts.com/lib/3/amcharts.js"></script>
      <script src="https://www.amcharts.com/lib/3/pie.js"></script>
      <script src="https://www.amcharts.com/lib/3/plugins/export/export.min.js"></script>
      <script src="https://www.amcharts.com/lib/3/serial.js"></script>
      <script src="https://www.amcharts.com/lib/3/serial.js"></script>
      <link rel="stylesheet" href="https://www.amcharts.com/lib/3/plugins/export/export.css" type="text/css" media="all" />
      <script src="https://www.amcharts.com/lib/3/themes/none.js"></script>

            <style>
          #leftSide {
            color: deepskyblue; font-family: Century Gothic, sans-serif; font-size: 25px; font-weight: 800; margin: 0 0 0; text-align: left; text-transform: uppercase; position:relative; left:60px;
          }

          #chartdiv {
            width: 150%;
            height: 475px;
            position:relative;
            right: 250px;
            bottom: 22px;
          }

          #chartdiv2 {
            width: 100%;
            height: 475px;
            position:relative;
            right: 70px;
            bottom: -40px;
          }



          ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
          }
          text {
            font-size:16px;
          }
          span {
            display: inline-block;
            vertical-align: middle;
            margin-top: -30px;
          }
          p {
            width: 100%;
            text-align: center;
            border-bottom: 1px solid #000;
            line-height: 0.1em;
            margin: 10px 0 20px;
          }
          span2 {
            background:#fff;
            padding:0 10px;
            font-family: Century Gothic, sans-serif;
          }
          h1 {    color: deepskyblue; font-family: Century Gothic, sans-serif; font-size: 25px; font-weight: 800; margin: 0 0 0; text-align: right; text-transform: uppercase;}

          .list-element {
            font-size:25px;
            padding:6px;
            padding-top:0;

            font: 20px/1.5 Century Gothic, sans-serif; font-weight: 510;
            border-bottom: 1px solid #D3D3D3;
            text-decoration: none;
            color: #000;
            display: inline-block;
            width: 200%;

            -webkit-transition: font-size 0.3s ease, background-color 0.3s ease;
            -moz-transition: font-size 0.3s ease, background-color 0.3s ease;
            -o-transition: font-size 0.3s ease, background-color 0.3s ease;
            -ms-transition: font-size 0.3s ease, background-color 0.3s ease;
            transition: font-size 0.3s ease, background-color 0.3s ease;
          }

          .list-element:last-child {
            border: none;
          }

          .list-element:hover {
            font-size: 25px;
            background-color: #fbfbfb;
          }
          .list-element:hover .atom-loader{
            height:75px;


          }
          .list-element:hover .atom-inner.atom-one {
            border-bottom: 4px solid #ff1a8c;
            border-top: 4px solid #ff1a8c;
            border-left: 4px dotted #ff1a8c;
            border-right: 4px dotted #ff1a8c;
          }
          .list-element:hover .atom-inner.atom-two {
            border-bottom: 4px solid #ff1a8c;
            border-top: 4px solid #ff1a8c;
            border-left: 4px dotted #ff1a8c;
            border-right: 4px dotted #ff1a8c;
          }

          .list-element:hover .atom-inner.atom-three {
            border-bottom: 4px solid #ff1a8c;
            border-top: 4px solid #ff1a8c;
            border-left: 4px dotted #ff1a8c;
            border-right: 4px dotted #ff1a8c;
          }

          .list-element:hover .atom-inner.atom-four {
            border-bottom: 4px solid #ff1a8c;
            border-top: 4px solid #ff1a8c;
            border-left: 4px dotted #ff1a8c;
            border-right: 4px dotted #ff1a8c;
          }


          html, body {
            height: 100%;
          }
          body{

            background-image: radial-gradient(top, circle cover, #aecddf, #426f88 80%);

            position: relative;
          }
          .atom-loader {
            position: relative;
            top: 2vw;
            left: 43vw;
            width: 50px;
            height: 50px;



            -webkit-backface-visibility: hidden;
            -webkit-transform: translateZ(0);
            -webkit-transition: height 0.3s ease, background-color 0.3s ease;
            -moz-transition: height 0.3s ease, background-color 0.3s ease;
            -o-transition: height 0.3s ease, background-color 0.3s ease;
            -ms-transition: height 0.3s ease, background-color 0.3s ease;
            transition: height 0.3s ease, background-color 0.3s ease;
            perspective: 600;

          }


          .atom-inner {
            position: absolute;
            width: 110%;
            height: 110%;


            box-sizing: border-box;
            border-radius: 50%;
            transform-style: preserve-3d;
          }

          .atom-inner.atom-one {
            left: 0%;
            top: 0%;
            animation: atom-rotate-one 5s linear infinite;

            border-bottom: 4px solid deepskyblue;
            border-top: 4px solid deepskyblue;
            border-left: 4px dotted deepskyblue;
            border-right: 4px dotted deepskyblue;

            width: 100%;
            height: 100%;
          }


          .atom-inner.atom-two {
            right: 0%;
            top: 0%;
            animation: atom-rotate-two 2.5s linear infinite;

            border-bottom: 4px solid deepskyblue;
            border-top: 4px solid deepskyblue;
            border-left: 4px dotted deepskyblue;
            border-right: 4px dotted deepskyblue;
          }


          .atom-inner.atom-three {
            right: 0%;
            bottom: 0%;
            animation: atom-rotate-three 5s linear infinite;

            border-bottom: 4px solid deepskyblue;
            border-top: 4px solid deepskyblue;
            border-left: 4px dotted deepskyblue;
            border-right: 4px dotted deepskyblue;

            transform: translateY(-50%);
          }

          .atom-inner.atom-four {
            right: 0%;
            bottom: 0%;
            animation: atom-rotate-four 2.5s linear infinite;

            border-bottom: 4px solid deepskyblue;
            border-top: 4px solid deepskyblue;
            border-left: 4px dotted deepskyblue;
            border-right: 4px dotted deepskyblue;
          }



          @keyframes atom-rotate-one {
            0% { transform: rotateX(60deg) rotateY(-50deg) rotateZ(0deg); }
            100% { transform: rotateX(60deg) rotateY(-50deg) rotateZ(360deg); }
          }

          @keyframes atom-rotate-two {
            0% { transform: rotateX(120deg) rotateY(30deg) rotateZ(0deg); }
            100% { transform: rotateX(120deg) rotateY(30deg) rotateZ(360deg); }
          }

          @keyframes atom-rotate-three {
            0% { transform: rotateX(70deg) rotateY(-20deg) rotateZ(0deg); }
            100% { transform: rotateX(70deg) rotateY(-20deg) rotateZ(360deg); }
          }

          @keyframes atom-rotate-four {
            0% { transform: rotateX(120deg) rotateY(60deg) rotateZ(0deg); }
            100% { transform: rotateX(120deg) rotateY(60deg) rotateZ(360deg); }
          }

          @keyframes center-rotate-one {
            0% { transform: rotateZ(0deg);
              transform-origin: calc(45% + 1em) calc(45% - 1em);

            }
            100% { transform: rotateZ(360deg);
              transform-origin: calc(45% + 1em) calc(45% - 1em);
            }
          }
        </style>

  <nav class="navbar" style=" border-bottom: solid; border-bottom-color: #abdffe; border-bottom-width: thin; text-align: center">
          <div class="container-fluid">
            <div class="navbar-header">
              <a class="navbar-brand" href="#" style="color: deepskyblue; padding-left: 20px; font-size: 20px; ">discover.ai</a>
            </div>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="#"style="background-color: transparent !important; color:deepskyblue; padding-right:50px">Export</a></li>
            </ul>
            <!--<button class="btn btn-danger navbar-btn">Button</button>-->
          </div>
        </nav>
    <div class="container">
        <div class="row">
            <div class="col-lg-6 col-sm-12" >
                <h1 id="leftSide">Top 100 Predicitons</h1>
                <div id="chartdiv"></div>
                <h1 id="leftSide">Prediction Distribution</h1>
                <div id="chartdiv2"></div>
            </div>
            <div class="col-lg-6 col-sm-12">
                <h1>Molecules binding probabilities</h1>

                <ul id="place_list">
                </ul>


            </div>

        </div>

    </div>

    </body>

    <script>
      $(function(){
        var ul = document.getElementById('place_list');


        for (var i = 0; i < molecules.length; i++) {
          var li = document.createElement("li");
          li.innerHTML = ('<div class="atom-loader"><div class="atom-inner atom-one"></div><div class="atom-inner atom-two"></div><div class="atom-inner atom-three"></div><div class="atom-inner atom-four"></div><div class="atom-inner atom-center-one"></div><div class="atom-inner atom-center-two"></div><div class="atom-inner atom-center-three"></div><div class="atom-inner atom-center-four"></div> </div>');
          var span = document.createElement("span");
          li.className = 'list-element'; span.appendChild(document.createTextNode(molecules[i].name + "\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0|\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0" + molecules[i].probability));
          li.appendChild(span);
          ul.appendChild(li);
          
          if (i > 10) {break;}
        }

      })
        
        """
        
        return val


    def get_bottom_half():    
        val = """
    
         var percentages = [
        {   "range" : "90-100%", "number" : 0.0, "color": "#FF0F00" },
        {   "range" : "80-90%", "number" : 0.0, "color": "#FF6600" },
        {   "range" : "70-80%", "number" : 0.0 , "color": "#FF9E01" },
        {   "range" : "60-70%", "number" : 0.0, "color": "#FCD202" },
        {   "range" : "50-60%", "number" : 0.0, "color": "#F8FF01"},
        {   "range" : "40-50%", "number" : 0.0, "color": "#B0DE09"},
        {   "range" : "30-40%", "number" : 0.0 , "color": "#04D215"},
        {   "range" : "20-30%", "number" : 0.0 , "color": "#0D8ECF"},
        {   "range" : "10-20%", "number" : 0.0 , "color": "#0D52D1"},
        {   "range" : "00-10%", "number" : 0.0 , "color": "#2A0CD0"}
      ];

      var getPercent = function(){
        for(var i = 0; i < 100; i++)
        {
          if(molecules[i].probability > 90)
            percentages[0].number = percentages[0].number + 1;
          else if(molecules[i].probability > 80)
            percentages[1].number = percentages[1].number + 1;
          else if(molecules[i].probability > 70)
            percentages[2].number = percentages[2].number + 1;
          else if(molecules[i].probability > 60)
            percentages[3].number = percentages[3].number + 1;
          else if(molecules[i].probability > 50)
            percentages[4].number = percentages[4].number + 1;
          else if(molecules[i].probability > 40)
            percentages[5].number = percentages[5].number + 1;
          else if(molecules[i].probability > 30)
            percentages[6].number = percentages[6].number + 1;
          else if(molecules[i].probability > 20)
            percentages[7].number = percentages[7].number + 1;
          else if(molecules[i].probability > 10)
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


         var getPercent2 = function(){
        for(var i = 0; i < molecules.length; i++)
        {
          if(molecules[i].probability > 90)
            percentages[0].number = percentages[0].number + 1;
          else if(molecules[i].probability > 80)
            percentages[1].number = percentages[1].number + 1;
          else if(molecules[i].probability > 70)
            percentages[2].number = percentages[2].number + 1;
          else if(molecules[i].probability > 60)
            percentages[3].number = percentages[3].number + 1;
          else if(molecules[i].probability > 50)
            percentages[4].number = percentages[4].number + 1;
          else if(molecules[i].probability > 40)
            percentages[5].number = percentages[5].number + 1;
          else if(molecules[i].probability > 30)
            percentages[6].number = percentages[6].number + 1;
          else if(molecules[i].probability > 20)
            percentages[7].number = percentages[7].number + 1;
          else if(molecules[i].probability > 10)
            percentages[8].number = percentages[8].number + 1;
          else
            percentages[9].number = percentages[9].number + 1;
        }
      }
      getPercent2();

      var chart = AmCharts.makeChart("chartdiv2", {
        "type": "serial",
        "theme": "light",
        "marginRight": 70,
        "dataProvider": percentages,
        "valueAxes": [{
          "axisAlpha":0,
          "position": "left",
          "title": "Molecules chance of binding to MAPK"
        }],
        "startDuration": 1,
        "graphs": [{
          "balloonText": "<b>[[range]]: [[number]]</b>",
          "fillColorsField": "color",
          "fillAlphas": 0.9,
          "lineAlpha": 0.2,
          "type": "column",
          "valueField": "number"
        }],
        "chartCursor": {
          "categoryBalloonEnabled": false,
          "cursorAlpha": 0,
          "zoomable": false
        },
        "categoryField": "range",
        "categoryAxis": {
          "gridPosition": "start",
          "labelRotation": 45
        },
        "export": {
          "enabled": false
        }

      });
    
        </script>
    
        </body>
    
    
            </html>
    
            """
            
        return val
