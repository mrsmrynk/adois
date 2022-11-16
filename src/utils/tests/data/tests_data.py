# @author: Maryniak, Marius - Fachbereich Elektrotechnik, Westfälische Hochschule Gelsenkirchen

parameters_get_coordinates = \
    [
        # region no quantization, no remainder
        ((512, 512, 1024, 1024),
         [(512, 768), (768, 768), (512, 1024), (768, 1024)]),
        ((512, -1024, 1024, -512),
         [(512, -768), (768, -768), (512, -512), (768, -512)]),
        ((-1024, -1024, -512, -512),
         [(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)]),
        ((-1024, 512, -512, 1024),
         [(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)]),
        ((-256, -256, 256, 256),
         [(-256, 0), (0, 0), (-256, 256), (0, 256)]),
        # endregion
        # region quantization, no remainder
        ((640, 640, 1024, 1024),
         [(512, 768), (768, 768), (512, 1024), (768, 1024)]),
        ((640, -896, 1024, -512),
         [(512, -768), (768, -768), (512, -512), (768, -512)]),
        ((-896, -896, -512, -512),
         [(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)]),
        ((-896, 640, -512, 1024),
         [(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)]),
        ((-128, -128, 256, 256),
         [(-256, 0), (0, 0), (-256, 256), (0, 256)]),
        # endregion
        # region no quantization, remainder
        ((512, 512, 896, 896),
         [(512, 768), (768, 768), (512, 1024), (768, 1024)]),
        ((512, -1024, 896, -640),
         [(512, -768), (768, -768), (512, -512), (768, -512)]),
        ((-1024, -1024, -640, -640),
         [(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)]),
        ((-1024, 512, -640, 896),
         [(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)]),
        ((-256, -256, 128, 128),
         [(-256, 0), (0, 0), (-256, 256), (0, 256)]),
        # endregion
        # region quantization, remainder
        ((640, 640, 896, 896),
         [(512, 768), (768, 768), (512, 1024), (768, 1024)]),
        ((640, -896, 896, -640),
         [(512, -768), (768, -768), (512, -512), (768, -512)]),
        ((-896, -896, -640, -640),
         [(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)]),
        ((-896, 640, -640, 896),
         [(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)]),
        ((-128, -128, 128, 128),
         [(-256, 0), (0, 0), (-256, 256), (0, 256)])
        # endregion
    ]

parameters_filter_cached_coordinates_empty_tiles_dir = \
    [([(512, 768), (768, 768), (512, 1024), (768, 1024)],
      [(512, 768), (768, 768), (512, 1024), (768, 1024)]),
     ([(512, -768), (768, -768), (512, -512), (768, -512)],
      [(512, -768), (768, -768), (512, -512), (768, -512)]),
     ([(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)],
      [(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)]),
     ([(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)],
      [(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)]),
     ([(-256, 0), (0, 0), (-256, 256), (0, 256)],
      [(-256, 0), (0, 0), (-256, 256), (0, 256)])]

parameters_filter_cached_coordinates_not_empty_tiles_dir = \
    [
        # region some tiles have already been downloaded
        ([(512, 768), (768, 768), (512, 1024), (768, 1024)],
         [(512, 768), (768, 768)]),
        ([(512, -768), (768, -768), (512, -512), (768, -512)],
         [(512, -768), (768, -768)]),
        ([(-1024, -768), (-768, -768), (-1024, -512), (-768, -512)],
         [(-1024, -768), (-768, -768)]),
        ([(-1024, 768), (-768, 768), (-1024, 1024), (-768, 1024)],
         [(-1024, 768), (-768, 768)]),
        ([(-256, 0), (0, 0), (-256, 256), (0, 256)],
         [(-256, 0), (0, 0)]),
        # endregion
        # region all tiles have already been downloaded
        ([(512, 1024), (768, 1024)],
         []),
        ([(512, -512), (768, -512)],
         []),
        ([(-1024, -512), (-768, -512)],
         []),
        ([(-1024, 1024), (-768, 1024)],
         []),
        ([(-256, 256), (0, 256)],
         [])
        # endregion
    ]
