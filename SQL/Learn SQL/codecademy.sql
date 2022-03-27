-- Project YANG ADA DI CODECADEMY

-- -- Melihat semua isi tabel
-- SELECT * 
-- FROM nomnom;

-- -- Melihat tabel neighborhood
-- SELECT DISTINCT neighborhood
-- FROM nomnom;

-- -- Melihat tabel cuisine
-- SELECT DISTINCT cuisine
-- FROM nomnom
-- WHERE cuisine = 'Chinese';

-- -- Melihat table restaurants review > 4
-- SELECT *
-- FROM nomnom
-- WHERE review >= 4;

-- -- Melihat tabel restoran yang ITALIAN dan harganya $$$
-- SELECT * 
-- FROM nomnom
-- WHERE cuisine = 'Italian'
--   AND price = '$$$'

-- -- Melihat tabel restoran yang ada kata meatballnya
-- SELECT *
-- FROM nomnom
-- WHERE name LIKE '%meatball%';

-- -- Melihat table yang didalamnya Midtown, Downton or ChinaTown
-- SELECT *
-- FROM nomnom
-- WHERE neighborhood = 'Midtown'
--   OR neighborhood = 'Downtown'
--   OR neighborhood = 'Chinatown';

-- -- Melihat grade health jika ada yang kosong
-- SELECT *
-- FROM nomnom
-- WHERE health IS NULL;

-- -- Membuat tabel TOP 10 rangking
-- SELECT *
-- FROM nomnom
-- ORDER BY review DESC
-- LIMIT 10;

SELECT name,
CASE
    WHEN review > 4.5 THEN 'Extraordinary'
    WHEN review > 4 THEN 'Excellent'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
END AS 'Passing Grade'
FROM nomnom;





