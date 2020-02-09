function createNodes(nodeList){
    var nodes = [];
    for(var i=0; i<nodeList.length;i++){
        var shape = "";
        var color = "";
        if(nodeList[i].type == "incubadoras"){
            color = "#6FB1FC";
            shape = "rectangle";
        }
        else if(nodeList[i].type == "parques_tecnologicos"){
            color = "#F5A45D";
            shape = "octagon";
        }
        else {
            color = "#EDA1ED";
            shape = "ellipse";
        }
        // se for a org do usuario
        if(nodeList[i].id == org_id) {
            color = "#00D46F";
           // size_index = 4;
        } else {
            //size_index = nodeList[i].size-1;    
        }
        node = {data:{id: 'node'+nodeList[i].id
            , name: nodeList[i].name
            , faveColor: color
            , faveShape: shape
            , faveColorBorder: "#333"
            , size: (((nodeList[i].size))) //sizeRange[size_index]
            , logo: ""}};
        nodes.push(node);
        
    }
    return nodes;
}

function getClass(keyword){
    for(var i=0;i<classesList.length;i++)
        if(keyword == classesList[i].name)
            return classesList[i].id; //JSON.stringify(
    return null
}

function createEdges(edgesArray, nodeList){
    var edges = [];
    for(var i=0; i<edgesArray.length;i++){
        if(hasNode(nodeList, edgesArray[i].source) && hasNode(nodeList, edgesArray[i].target)){
            edges.push({
                data: {source: 'node'+edgesArray[i].source
                    , target: 'node'+edgesArray[i].target
                    , weight: (edgesArray[i].weight) 
                    , strength: (edgesArray[i].weight)
                    , faveColor: edgesArray[i].lineColor } 
            });
        }
    }
    return edges;
}

function hasNode(nodeList, nodeId){
    for (var i=0; i < nodeList.length; i++){
        if(nodeList[i].id == nodeId){
            return true;
        }
    }
    return false;
}

function createElements(nodeList, edgeList){
    return {nodes:createNodes(nodeList)
            , edges: createEdges(edgeList, nodeList)};
}

$(function(){
    var nodeCSS = {'shape': 'data(faveShape)', 'width': 'data(size)', 'height': 'data(size)', 'content': 'data(name)', 'text-valign': 'center' ,'text-outline-width': 2, 'text-outline-color': 'data(faveColor)', 'background-color': 'data(faveColor)' , 'border-width': 2, 'border-color': '#333', 'color': '#fff'}; //,'background-image': 'data(logo)'
    var edgeCSS = {'curve-style': 'bezier', 'opacity': 0.666, 'width': 'data(strength)', 'target-arrow-shape': 'none', 'source-arrow-shape': 'none', 'line-color': 'data(faveColor)', 'source-arrow-color': 'data(faveColor)', 'target-arrow-color': 'data(faveColor)'};
    var selectedCSS = {'border-width': 3, 'border-color': '#333'}; //'#6FB1FC'
    var questionableCSS = {'line-style': 'dotted', 'target-arrow-shape': 'diamond'};
    var fadedCSS = {'opacity': 0.25, 'text-opacity': 0};
    
    var keywordsArray = new Array();

    var cy = cytoscape({container: $("#cy")
        , style: [{selector: 'node', css: nodeCSS}
                , {selector: 'edge',css: edgeCSS}
                , {selector: ':selected', css: selectedCSS }
                , {selector:'edge.questionable', css: questionableCSS}
                , {selector: '.faded' ,css:fadedCSS}
            ]
        , elements: createElements(nodeList, edgeList)  
        , maxZoom:2.0
        , minZoom:0.1
        , ready: function(){
            window.cy = this;
            this.layout({name: 'fcose'
                 // Whether to animate while running the layout
                , animate: true
                // Number of iterations between consecutive screen positions update (0 -> only updated on the end)
                , refresh: 20
                // Whether to fit the network view after when done
                , fit: true
                // Padding on fit
                , padding: 30
                // Whether to use the JS console to print debug messages
                , debug: false
                // Node repulsion (non overlapping) multiplier
                , nodeRepulsion: 400000
                // Node repulsion (overlapping) multiplier
                //, nodeOverlap: 10
                // Ideal edge (non nested) length
                //, idealEdgeLength: 10
                // Divisor to compute edge forces
                //, edgeElasticity: 100
                // Nesting factor (multiplier) to compute ideal edge length for nested edges
                //, nestingFactor: 5
                // Gravity force (constant)
                , gravity: 50
                // Maximum number of iterations to perform
                , numIter: 1000
                // Initial temperature (maximum node displacement)
                , initialTemp: 200
                // Cooling factor (how the temperature is reduced between consecutive iterations
                , coolingFactor: 0.95
                // Lower temperature threshold (below this point the layout will end)
                , minTemp: 1.0                      
            }).run();
        }
    });

var metricsList = [];
var pageRank = cy.elements().pageRank();
var dcn = cy.$().dcn();
var ccn = cy.$().ccn();
var bc = cy.$().bc();

for (var i=0;i<nodeList.length;i++){
    metricsList.push({node_id: nodeList[i].id
        , degree: dcn.degree('#node'+nodeList[i].id)
        , closeness: ccn.closeness('#node'+nodeList[i].id)
        , betweenness: bc.betweenness('#node'+nodeList[i].id)
        , pageRank: pageRank.rank('#node'+nodeList[i].id)
        });
}
for (var i=0;i<metricsList.length;i++){
    var metric = metricsList[i];
    $("#degree"+metric.node_id).text(metric.degree.toFixed(4));
    $("#closeness"+metric.node_id).text(metric.closeness.toFixed(4));
    $("#betweenness"+metric.node_id).text(metric.betweenness.toFixed(4));
    $("#pagerank"+metric.node_id).text(metric.pageRank.toFixed(4));
}


$("#total_nodes").text(nodeList.length);
$("#total_edges").text(edgeList.length);
$("#density").text(edgeList.length/((nodeList.length*(nodeList.length-1))/2));

$("#btAddKey").click(function(){
        var key = $("#keySearch").val();
        var objKey = getClass(key);
        if(objKey) {
            keywordsArray.push(objKey);
            $("#hd_keywords").val(keywordsArray);

            $("#keyword-search")
                .append($("<div/>")
                    .addClass("alert alert-secondary alert-dismissible fade show col-md-2 float-left keywordItem")
                    .attr("role", "alert")
                    .text(key)
                    .append($("<button />")
                        .attr("type", "button")
                        .addClass("close btn-close")
                        .attr("data-dismiss", "alert")
                        .attr("aria-label", "Close")
                        .append($("<span />")
                            .attr("aria-hidden", "true")
                            .html("&times"))
                    )
                );
        }
        $("#keySearch").val("");
        $("#keySearch").focus();
    });

$("#org_stats a").click(function(){
    var link = $(this).attr("href");
    $.ajax({
        url:link 
        , contentType: "charset=UTF-8"
    }).done(function(data){
        var dataHTML = $.parseHTML(data);

        var org_name = $(dataHTML).find("#org_name").text();
        var org_logo = $(dataHTML).find("#org_logo").text();
        var org_type = $(dataHTML).find("#org_type").text();
        org_type = (org_type!="")?" - <i>"+org_type+"</i>":org_type;
        var org_status = $(dataHTML).find("#org_status").text();
        var org_description = $(dataHTML).find("#org_description").html();
        var org_address = $(dataHTML).find("#org_address").text();
        var org_common_skill_list = $(dataHTML).find("#common_education_list").html();
        var org_other_skill_list = $(dataHTML).find("#other_education_list").html();

        var classes= $(dataHTML).find("#classes").html();
        $("#org_name").html(org_name+org_type);
        $("#logo").attr('src', org_logo);
        $("#description").html(org_description);
        $("#address").text(org_address);
        $("#status").text(org_status);
        $("#org_common_skill_list").empty();
        $("#org_common_skill_list").append(org_common_skill_list);
        $("#org_other_skill_list").empty();
        $("#org_other_skill_list").append(org_other_skill_list);
        
    });
})

$("#type_all").click(function(){
    console.log($("#type_all").val());
    $(".org_status").val($("#type_all").val());
});

$("#ecobuider_all").click(function () {
    $('.chk_ecobuilder').prop('checked',true);
    $("input[name=ecobuilder").prop('checked', $(this).prop('checked'));
});

$("#layoutRandom").click(function(){
    var layout = cy.layout({
        name: 'random'
        , animate: true
        , animationDuration: 1000
        , gravity: 80
        , numIter: 1000
        , initialTemp: 200
        , coolingFactor: 0.95
        , minTemp: 1.0
    });
    layout.run();        
});          
          
$("#layoutArbor").click(function(){
    var layout = cy.layout({
        name: 'fcose'
        , quality: 'default'
        , randomize: true
        , animationEasing: 'ease-out'
        , gravity: 80
        , numIter: 1000
        , initialTemp: 200
        , coolingFactor: 0.95
        , minTemp: 1.0
    });
    layout.run();        
});

});