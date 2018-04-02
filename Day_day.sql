Select 
	day.media,
	day.account_no,
	day.from_date,
	day.to_date,
	day.row_type,
	day.device,
	day.network,
	day.day,
	day.impressions,
	day.clicks,
	day.conversions,
	day.cost,
	day.sort_seq 
From 
	standard_report.day as day
Where
	day.media = #prompt('media', 'string')#
	and day.account_no = #prompt('account_no', 'string')#
	and day.from_date = #prompt('from_date', 'date')#
	and day.to_date = #prompt('to_date', 'date')#
	and day.row_type = #prompt('rowtype', 'string')#
	and day.device = #prompt('device', 'string')#
	and day.network = #prompt('network', 'string')#
	