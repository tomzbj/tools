--- Changes ---
现在会生成__bom.csv和__coord.csv两个文件.

--- Original ---
1. Allegro 菜单点Tools, Reports.
2. 从Available Reports里找Placed Component Report, 双击让它跑到下面框里. 
3. 选中Write Report, 点Report. 此时会在.brd所在目录下生成一个pcp_rep.rpt.
4. 执行jlc_bom_coord.py, 会生成__pcp_rep_jlc.csv. JLC SMT下单的坐标文件和BOM文件用这一个文件即可.
