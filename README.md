# wafermap_iiivwfmod

This is a repository to plot a wafer map.

Here is the requirement for the code.
- Import csv file in the `data` folder using Pandas
- Filter the table with the conditions below:  
  - Lot: AL810962
  - Wafer: D08
  - TestSite: IIIV_LMZC_IIIV230_JT100
- Plot X: Row, Y: Column, Z: `VpiL@0V [V.cm]` using [wafer map repo](https://github.com/dougthor42/wafer_map)
- Additional info.
  - die_size_X = 25870 um
  - die_size_Y = 13820 um
  - dia = 300000 um
