function drawChart() {
	var margin = {top: 20, right: 20, bottom: 70, left: 40},
		width = 600 - margin.left - margin.right,
		height = 300 - margin.top - margin.bottom;

	// Parse the date / time
	var	parseDate = d3.time.format("%Y-%m-%d").parse;

	var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

	var y = d3.scale.linear().range([height, 0]);

	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom")
		.tickFormat(d3.time.format("%Y-%m-%d"));

	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("left")
		.ticks(10);

	var tip = d3.tip()
	  .attr('class', 'd3-tip')
	  .offset([-10, 0])
	  .html(function(d) {
		return "<strong>Avg. Wait:</strong> <span style='color:orangered'>" + d.avg_wait_time + "</span><br><strong>Visits:</strong> <span style='color:orangered'>" + d.visit_count + "</span>";
	  })

	var svg = d3.select("body").append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	  .append("g")
		.attr("transform", 
			  "translate(" + margin.left + "," + margin.top + ")");

	svg.call(tip);

	data.forEach(function(d) {
		d.visit_date = parseDate(d.visit_date);
		d.avg_wait_time = +d.avg_wait_time;
	});
	
	x.domain(data.map(function(d) { return d.visit_date; }));
	y.domain([0, d3.max(data, function(d) { return d.avg_wait_time; })]);

	svg.append("g")
	  .attr("class", "x axis")
	  .attr("transform", "translate(0," + height + ")")
	  .call(xAxis)
	.selectAll("text")
	  .style("text-anchor", "end")
	  .attr("dx", "-.8em")
	  .attr("dy", "-.55em")
	  .attr("transform", "rotate(-90)" );

	svg.append("g")
	  .attr("class", "y axis")
	  .call(yAxis)
	.append("text")
	  .attr("transform", "rotate(-90)")
	  .attr("y", -30)
	  .style("text-anchor", "end")
	  .text("Average Wait (min)");

	svg.selectAll("bar")
	  .data(data)
	.enter().append("rect")
      .attr("class", "bar")
	  .attr("x", function(d) { return x(d.visit_date); })
	  .attr("width", x.rangeBand())
	  .attr("y", function(d) { return y(d.avg_wait_time); })
	  .attr("height", function(d) { return height - y(d.avg_wait_time); })
	  .on('mouseover', tip.show)
	  .on('mouseout', tip.hide)
    }

