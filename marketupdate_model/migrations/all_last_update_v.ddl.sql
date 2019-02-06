--
-- QUERY SOTTESA ALLA VIEW all_last_update_v
--
select row_number() over () as id,
	val.value as val_value, 
	val.unit as val_unit, 
	val.precision as val_precision, 
	val.val_format as val_format, 
	val.val_sequence as val_sequence, 
	val.description as val_description,
	sym.name as sym_name,
	sym.description as sym_des,
	cat.name as cat_name,
	cat.description as cat_des,
	upd.pub_date as pub_date,
	upd.pub_hour as pub_hour
from marketupdate_model_update upd, marketupdate_model_category cat, marketupdate_model_symbol sym, marketupdate_model_value val
where 
	val.symbol_id = sym.id and
	sym.category_id = cat.id and
	cat.update_id = (
		select id from marketupdate_model_update
		where concat(pub_date, pub_hour) = 
		(select max(concat(pub_date, pub_hour)) from marketupdate_model_update)
) 
	and upd.id = cat.update_id
order by cat.id, sym.id, val_sequence
