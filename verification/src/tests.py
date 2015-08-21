"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Rank_01": [
        {
            "input": ["How are you doing?",
                      "I'm fine. OK.",
                      "Lorem Ipsum?",
                      "Of course!!!",
                      "1234567890",
                      "0        0",
                      "1234567890",
                      "Fine! good buy!"],
            "answer": 3,
            "explanation": [[1, 9], [2, 5], [3, 2]],
        },
        {
            "input": ["WoW",
                      "A A",
                      "WoW"],
            "answer": 1,
            "explanation": [[1, 1]]
        },
        {
            "input": ["HELLO",
                      "O O O",
                      "NIGHT",
                      "O O O",
                      "IDDQD"],
            "answer": 4,
            "explanation": [[1, 1], [1, 3], [3, 1], [3, 3]]
        },
        {
            "input": ["HELLO",
                      "O   O",
                      "NIGHT",
                      "O   O",
                      "IDDQD"],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['Lorem ipsum dolor', 'sit amet,', 'consectetuer', 'adipiscing elit.', 'Aenean commodo',
                      'ligula eget dolor.', 'Aenean massa. Cum', 'sociis natoque', 'penatibus et magnis',
                      'dis parturient', 'montes, nascetur', 'ridiculus mus. Donec', 'quam felis,', 'ultricies nec,',
                      'pellentesque eu,', 'pretium quis, sem.', 'Nulla consequat', 'massa quis enim.',
                      'Donec pede justo,', 'fringilla vel,'],
            "answer": 11,
            "explanation": [[1, 3], [3, 10], [5, 11], [8, 9], [8, 12], [9, 3], [10, 7], [11, 9], [12, 4], [13, 9],
                            [15, 7]]
        },
        {
            "input": ['qwerty asdfg ghjkl 123'],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1', 'asd', '0 1',
                      'asd', '0 1', 'asd', '0 1', 'asd', '0 1'],
            "answer": 9,
            "explanation": [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1], [11, 1], [13, 1], [15, 1], [17, 1]]
        },
        {
            "input": ['hi hi', 'hello', 'hello', 'hello', 'hello', 'hello', 'by by'],
            "answer": 0,
            "explanation": []
        },
        {
            "input": [' X ', 'XXX', ' X ', 'X X', ' X '],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['J  ck wU phP  UZfhHx', 'YNJ ugWNxKsPRasldco', 'hnIsUlWVO EhIyoNwLNZ', 'JEbloQ',
                      'XWrjMl B CAOR hZoJ', 'fMbJYeWgZHdbrgzcstd', 'ycY GyuS Sblj WB', 'fScUFqMKPOZ I', 'ioBkDQUL',
                      'QCV UweAY zm', ' QR QOe Ew lBGRvlnK', 'LeHduzsbakBufXD', ' AQGRp UtLGYS', 'nnDywuYwZTsHinW WJ',
                      'jLWKFjkUYfuZL okJz', 'HhdAZdhcKpiYkAWxg', 'zAVNZOzyE ', 'QRkRdf', 'hutrJFUvrFe'],
            "answer": 5,
            "explanation": [[6, 3], [6, 8], [10, 7], [12, 6], [14, 13]]
        },
        {
            "input": ['V WPLWPpGr aJYUIA ', 'zSemLl', 'kK NgKu', 'XXeZlysMeDB U', 'PBUyuNzyPkUzK'],
            "answer": 1,
            "explanation": [[2, 2]]
        },
        {
            "input": ['pcrcfdz Yzw oL zOPZg', 'UtQr RkKux BM', ' Xb Rqg', 'fcFddLEvLQA j Jo nds', 'peFeus'],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['ouisZGL', 'k taYLyLxAmjb p', 'izyzgfqfV', 'ykSmmdOecDs', 'm Brdmez cAGox FDJcF'],
            "answer": 1,
            "explanation": [[1, 1]]
        },
        {
            "input": ['DtCiUc  VfEez ', 'yabe  FhCL', 'HVSxuyZIq OOv I', 'wTbaFxjNwBQ zyhXvo', 'MOpDnEAry JlSdmfCtA',
                      'XSSd TsjfEVKBo  ', 'lDzreTMcnIlCe U ', 'yhWyh dEfLW p', 'F HDms paR'],
            "answer": 3,
            "explanation": [[3, 11], [4, 9], [5, 4]]
        },
        {
            "input": ['MVSOysemW', 'rOLHVMczVu', 'RGkMBhVOv', 'pQHHH Fucu oJi ', ' rrmyHRXQJJRFk', 'liMhzQ',
                      'llbiQNjgSabywB', 'kq Jy nIJRDMbeDeM ', 'G knT', ' wQZprjSA', 'EszreYcyDI oK', 'spKstKAfmz Gfwyf',
                      ' Xhydvh uKby G', 'Po twD  qFrHiyzUo', 'WHcMcHfKV xVpMB RM', 'XIIcrkhais X', 'CKNGDa heTnI',
                      'GsZFiAOHVONPm ', ' QwOXJyXtxz', 'GWcOlL  '],
            "answer": 4,
            "explanation": [[3, 5], [12, 12], [13, 2], [16, 6]]
        },
        {
            "input": ['RgUSvLyebFhXtmtj wjL', 'TP VLSCqOZy ', 'JR  WlHvxuYhsuRq', 'LJPdoojV', 'VPBH  P R W jYYuMS',
                      'adxzbbpL ', 'PRJIEuJEpOrUStSvxEjt', 'fE tBDSMFU', 'TySGdtaqn G Un', 'z WvprhnLBrK ',
                      ' hYo BDMIXikW', 'KJNbrAC KfFcaGRUC s', 'ckmyykybYpB L', 'rjqRz c', 'iAkXD',
                      'JILvumRBwtloIIB hRWC', 'jyPrFk tQaQNyKZDr', 'myhoriXxeVMAnrD', 'nKiRpu', 'neFokQ'],
            "answer": 4,
            "explanation": [[7, 2], [10, 4], [11, 7], [16, 6]]
        },
        {
            "input": ['qFcPHRwCwfFL', 'GkHsMXsfm ', 'KukHZYJwilobSiJbpe', 'RxFvXCrinuBmT ', 'qoGi  ugXWANYEEc',
                      'VoQHhA ', 'gqeeNyGvN', 'gfpfhmEOqgyexSD', 'RQinQyZOU', 'WwuaXsClH xbh', '  zMAL  '],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['ifXZCui  SzG  c',
                      'QrY dnDT',
                      'Wrn itGs x',
                      'I SUSafs',
                      'awU Gr uhlgokJbA',
                      'm RSxB Y',
                      'PSnIlMAASHxk qExWmKH',
                      'Wduz tYhzEQfLB',
                      'zpgSfz',
                      'iFjVlC ZwmGWTG',
                      'aEfzWMoVwUVxUaphbJEC',
                      'vfghLjw caSdb',
                      'XQnhIKmASbD YE',
                      'DpbLfAHJNlZb',
                      'QEaSTUuksSwZsWy'],
            "answer": 5,
            "explanation": [[3, 1], [4, 3], [5, 1], [7, 4], [11, 7]]
        },
        {
            "input": [' VqYICFfGZiAGIpIyt', 'ZOrwpKvepCWU ', 'UVb JsizC', 'bTiPknDgrxB UlEWTw', 'wAC OPPIXBqqLsBObBCD',
                      'AgPTPxRXptcTuviW', 'l qgjx Xd o ', 'LwlUwoYxytSK Gf', ' FkiaAY oHiLumStzF', ' XM tZOvTlFA ',
                      'BCJkZWBZ', 'RjnNo yrptz', 'EGliuKSSxfItYNwLBpVP', 'UKLZO ', 'zPCbaRMBzK'],
            "answer": 8,
            "explanation": [[2, 3], [4, 3], [6, 1], [6, 6], [6, 9], [8, 7], [9, 3], [11, 5]]
        },
        {
            "input": ['cwzkoJwDYWDAthXQuB', 'hxN dWTiAT', 'YcO C L Mgv floTsa', 'zCEScCL o iNraU', 'oH BAcrXwkuiTSQr',
                      'AJSNNhLhPPn', 'lfHeTohrvYx', 'SQ rUos wolYX  amI', 'qowOsX LGES E', 'TC UqKDdAJBrOV',
                      'yIqGSz qbw I', 'dsOcpE JE w', 'HsgwClUcf dzMoj', 'M tkuIKfSZIpYpu n', 'ACZDyE',
                      ' mkJjTJQlCXorGSkblch', 'Jap TNyJ', 'q xhLpmQa nX', 'U Bt mkbWAdGZHItKEB', 'UdfKtPEk SLaOFTSGV'],
            "answer": 9,
            "explanation": [[2, 5], [3, 9], [4, 2], [7, 2], [8, 11], [9, 2], [13, 1], [16, 3], [18, 4]]
        },
        {
            "input": ['mRiRX', 'bcwkok', 'NCsgmVJagzXV Wb', 'Bs wd', 'oy eJBztwY  sYJpt eY', 'J Ay rNl K Ryh',
                      'bbVSeuRcPTLE'],
            "answer": 2,
            "explanation": [[5, 4], [5, 8]]
        },
        {
            "input": ['Mrfq  kdKcFJkqJIlEo', 'EI uMJL JM', 'gX qTfGq', 'VY bhw PSTwVWs Lq', 'hJanR fugWlJJUo',
                      'ZwnfCk ijEs ', 'SVcACdj', 'n CO L iRS LHRcWRVs', ' bgSVqkT CC ', 'GDMr TIQNXhyo', ' YXAgzC',
                      'gXWNeYYXLxLcksYzAqor', 'gHmfreC Ro GDmynI', 'BrShm F', 'ripg QVjUIoYnOqA', 'hCo J MXPCuYoL'],
            "answer": 3,
            "explanation": [[7, 4], [8, 8], [9, 4]]
        },
        {
            "input": ['AXfYiJuSadayKm', 's NqIFRoP', 'OONJQvogM F at', 'CFH b plLeIrIM', 'XEq hySp  uTLPwvZuiF',
                      'J gVGXexKsvoIIjt', 'OI MAq jMCtFu', 'aLU mSdLHEdPkJF', 'KriSsecGefhs qaHD', 'lwrp ', 'gWPTOQg',
                      'NfDMBgwKiFT', 'JR IVDOXihRNv', 'GBL BUsrFyMMJfy O', 'PJBnDaeWEgVK BVX JSD', 'KgWIp',
                      'bw qjAv mMzwNE fbER '],
            "answer": 3,
            "explanation": [[1, 1], [3, 5], [6, 6]]
        },
        {
            "input": ['N QYhJhxdIepekpEwKf', 'mUWvjp L cV', 'HDGwsbXb Da', 'OJnr  NSyswW fI', 'KYoJRuPTT Q ', 'rkXiGA',
                      'yWv  hblGvaOev', 'FbFrOUkPvpWqsE', 'eAZFcraUMLvu zYweoRF', 'IwpkxWgXFOYwTFVn sbR', ' av Td',
                      'st Af i', 'XYgDLoNFugAM', 'GyHngphe GwCmHrj', ' hLgGi BdI', 'gCwrBfcVgmtCWG'],
            "answer": 4,
            "explanation": [[1, 6], [8, 12], [13, 8], [14, 6]]
        },
        {
            "input": ['cshcF XJDOvutxpQyQy', 's  lqAjuKIK avAponM', 'QqPPBPjGtS Vfu XNPJ', ' HonikAbRnsA',
                      ' BkMiOlzzbP ', 'MNsIYbJ mAHE', 'FMnyvCBLppjCjyS', 'ngHZEtbsFnVBJqS', 'ri dVDHM WiAO RksX',
                      'Vy VnTbmobsmyuR', 'IEDVoXYOEOAMKHKJD', 'IZ lmR SjI', 'qs pKzDXnM zWaIyg', 'ZiLQV',
                      'mfkT Hqz qkyhxDP', 'aQPmBF', 'UDk ZwgYSy qZ tCn'],
            "answer": 4,
            "explanation": [[5, 7], [8, 8], [8, 13], [11, 6]]
        },
        {
            "input": ['MrqInIZLV PnXTpx', 'LYnWWpn IpH', 'rMvKD NAC O ', 'iepsDO', 'yozGNyFTrGFWXw URr'],
            "answer": 1,
            "explanation": [[1, 7]]
        },
        {
            "input": ['H rhrf', 'YMrQemz', 'kYwEiU', 'SrqY OQlyjSXwgjNPFPp', 'oKZfqxIfpIzeczGxYneE', 'PyGq Ox   ',
                      'ECwqRmqMyVlaA', 'o VcgNh', 'gA b fWQM', 'IslWf FacSf', 'yQgEskgNri', 'xtJ dJWPFp', 'mk jaKiVT',
                      'v atoXXbA ORkaZlu'],
            "answer": 2,
            "explanation": [[3, 4], [5, 4]]
        },
        {
            "input": ['wdeMONAByH LGOrJ', 'MAVhnYwl', 'BEJoesroLTp UIVQMcGO', 'g IdnGIx jhH', 'K xQg LE', 'Z o pf',
                      'TrpJdxvKMw', 'MFzpnXGTS', 'ozOzmSabgNwXbAJnHfA', 'hmX KKFejcXax', 'ygKDlZRrMHytzpk Td',
                      'KlRfQeD  iH', ' XS scm', 'ksuMxkHweznXR', 'vUv jx E'],
            "answer": 3,
            "explanation": [[5, 3], [9, 3], [12, 3]]
        },
        {
            "input": ['JEqFNG nrvTpixf', ' AhDgh', ' cec HjJOLmFk', 'pQwAo MaVhRQiMwzqrrZ', 'd OozXECVuUTrk rFPv',
                      'MH vHPSoy Jozfx xqV', 'MU UfdW r dAbj', 'hQdMPaGPPyfKUA', ' F   yESFHlgxIfm', 'dPSebVEJAYr',
                      'GkD DBCXU', ' AqJjMukfbmz OlgR', 'DjCEw TsAiihbLDig ', 'XUgVfMYZhDxaZAE', ' c QwqiSFNGWYraBXo',
                      'vTBpTkKTyR qXFcjihE'],
            "answer": 4,
            "explanation": [[6, 7], [10, 3], [12, 5], [14, 2]]
        },
        {
            "input": ['yFLVLDVQMYQAgsLf', 'JfarV ', 'ayKo iQBqZTAaRNBZe', 'H  SHbW HfjkBIY s  ', 'bbv fbAUt ', 'ZSniB',
                      'PAlhgp h  KGvsiJB', 'qONN  ZjDVVxezJH', 'HpePLtjmZKNIBLEGq zc'],
            "answer": 1,
            "explanation": [[3, 7]]
        },
        {
            "input": ['BTDlXjHue pwYT', 'UKYYn pHETRxTsE', ' SnfxtomdBDL', 'JxAAN', 'Ogp bIfPT', 'BB  mrSNEFeSYr',
                      'X RGkDZeAsutFPJhBXrn', 'D CXjazixu', 'UTwOGesrHx GJPIk', 'ou gylR r', 'nHV  h', ' lgFXgnmXuSSxu',
                      'T eQwxpo l', 'duGuxH BpAA Xjb  BZf', 'nbLADAni EgbwnhH AG', '  FKdI'],
            "answer": 3,
            "explanation": [[1, 5], [12, 8], [13, 6]]
        },
        {
            "input": ['ji R qfyHZ', 'IbfgmQwgiM', 'kcHVcacwuXOWnOS', 'YEkIQMD', 'SKA SS FfBXD PaVMz',
                      'ud  XGvKgoEDoN  ', 'LWtoB CpSGSAsFb', 'DohsV', 'vpeWRNuBTy', 'OioEiZ', 'lsNBApDG cKhp GRk',
                      'I tXVNTM SP brwA ', 'S ZwiLogz', 'OJgZFiOcJirfowTGnSO', 'xScIMp SVyKsOZgJucb',
                      'D ksoV fYj bhRJQElTN', 'zzehxwpS qHt', 'bNf  mEJApdDerBA', 'XSBuyH'],
            "answer": 3,
            "explanation": [[15, 1], [15, 10], [16, 8]]
        },
        {
            "input": ['oUDqT ypZ rfhqZaXFA', 'WChNwvoRAYP', 'iZntxamJQyiQc', 'jqeZp', ' zatYCsI', 'fiEoPsRL',
                      'TP bnKdhrBhDTA KTgV '],
            "answer": 0,
            "explanation": []
        },
        {
            "input": ['mVTaW oqOFEUmE qe', 'MCpuBerfg keqgt', 'MIqCItwAvYdSyeVYt', 'hRl aW', 'nxYOsZGbXoGM',
                      'RUlZTt sfsGLFiGPe', 'tnbcMWNkjk', 'G Tzg  LTkoxpv h p'],
            "answer": 3,
            "explanation": [[1, 9], [3, 3], [5, 6]]
        },
        {
            "input": ['AjzAROlo ', ' B qsgw  VIhxp uF', 'bMZr rZC'],
            "answer": 1,
            "explanation": [[1, 2]]
        },
        {
            "input": [' CRZ usONil', 'htdNkOIlVGXWM LNh', 'jjxqzajBLwc WnZTLb K', 'nIGCe', 'IJEgDn', 'bAOp lEgnpXw Qym',
                      'uhOBlQ'],
            "answer": 1,
            "explanation": [[5, 4]]
        },
    ]
}
