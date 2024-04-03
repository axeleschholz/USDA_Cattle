
DROPPED_ATTRIBUTES = ['report_narrative', 'group', 'category', 'comments_commodity',
                      'market_location_name', 'market_location_city',
                      'market_location_state', 'market_type',
                      'market_type_category', 'report_narrative', 'office_code',
                      'office_city', 'office_name']

REPORT_SLUGS = [2006, 2056, 1907, 1704, 1933, 2041, 1976, 2167, 1895, 2193, 1821, 2111, 1778,
                1860, 1784, 2091, 2100, 1831, 1919, 1963, 2027, 2063, 1955, 2039, 2187, 2240, 2106,
                ]

EXCLUDED_COLUMNS = ['report_title', 'slug_name', 'slug_id']

STORED_COLUMNS = ['report_date', 'report_begin_date', 'report_end_date', 'published_date',
                  'office_state', 'slug_id', 'slug_name', 'report_title', 'commodity',
                  'class', 'frame', 'muscle_grade', 'quality_grade_name', 'lot_desc',
                  'freight', 'price_unit', 'age', 'pregnancy_stage', 'weight_collect',
                  'offspring_weight_est', 'dressing', 'yield_grade', 'head_count',
                  'avg_weight_min', 'avg_weight_max', 'avg_weight', 'avg_price_min',
                  'avg_price_max', 'avg_price', 'weight_break_low', 'weight_break_high',
                  'receipts', 'receipts_week_ago', 'receipts_year_ago', 'final_ind']

PRICE_COLUMNS = ['avg_price_min', 'avg_price_max', 'avg_price']
DATE_COLUMNS = ['report_date', 'report_begin_date',
                'report_end_date', 'published_date']
