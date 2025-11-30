counties = [
    {
        "county_name": "Alameda County",
        "population": 1605217,
        "employment": 1325022,
        "res_consumption_mwh": 2849120,
        "commercial_consumption_mwh": 4495581,
        "ind_consumption_mwh": 2142646
    },
    {
        "county_name": "Contra Costa County",
        "population": 1107925,
        "employment": 647572,
        "res_consumption_mwh": 2633615,
        "commercial_consumption_mwh": 2462782,
        "ind_consumption_mwh": 959797
    },
    {
        "county_name": "El Dorado County",
        "population": 183000,
        "employment": 90046,
        "res_consumption_mwh": 533807,
        "commercial_consumption_mwh": 406674,
        "ind_consumption_mwh": 263060
    },
    {
        "county_name": "Fresno County",
        "population": 963160,
        "employment": 508312,
        "res_consumption_mwh": 2350782,
        "commercial_consumption_mwh": 2206816,
        "ind_consumption_mwh": 1244892
    },
    {
        "county_name": "Kern County",
        "population": 871337,
        "employment": 381006,
        "res_consumption_mwh": 1998148,
        "commercial_consumption_mwh": 1971548,
        "ind_consumption_mwh": 2040383
    },
    {
        "county_name": "Los Angeles County",
        "population": 10057155,
        "employment": 7743432,
        "res_consumption_mwh": 20815748,
        "commercial_consumption_mwh": 35921616,
        "ind_consumption_mwh": 10157974
    },
    {
        "county_name": "Merced County",
        "population": 265001,
        "employment": 86268,
        "res_consumption_mwh": 634036,
        "commercial_consumption_mwh": 450771,
        "ind_consumption_mwh": 1732436
    },
    {
        "county_name": "Orange County",
        "population": 3132211,
        "employment": 2965204,
        "res_consumption_mwh": 6763272,
        "commercial_consumption_mwh": 9700359,
        "ind_consumption_mwh": 4489462
    },
    {
        "county_name": "Placer County",
        "population": 370571,
        "employment": 284216,
        "res_consumption_mwh": 1222198,
        "commercial_consumption_mwh": 1134317,
        "ind_consumption_mwh": 368438
    },
    {
        "county_name": "Riverside County",
        "population": 2323892,
        "employment": 1107408,
        "res_consumption_mwh": 6343012,
        "commercial_consumption_mwh": 11446764,
        "ind_consumption_mwh": 1345934
    },
    {
        "county_name": "Sacramento County",
        "population": 1479300,
        "employment": 932682,
        "res_consumption_mwh": 4421932,
        "commercial_consumption_mwh": 3703213,
        "ind_consumption_mwh": 716992
    },
    {
        "county_name": "San Bernardino County",
        "population": 2106754,
        "employment": 1164560,
        "res_consumption_mwh": 4526519,
        "commercial_consumption_mwh": 6469079,
        "ind_consumption_mwh": 2748419
    },
    {
        "county_name": "San Diego County",
        "population": 3253356,
        "employment": 2496738,
        "res_consumption_mwh": 5828515,
        "commercial_consumption_mwh": 7064821,
        "ind_consumption_mwh": 3206255
    },
    {
        "county_name": "San Francisco County",
        "population": 850282,
        "employment": 1251464,
        "res_consumption_mwh": 1326629,
        "commercial_consumption_mwh": 4236898,
        "ind_consumption_mwh": 153771
    },
    {
        "county_name": "San Joaquin County",
        "population": 714860,
        "employment": 354322,
        "res_consumption_mwh": 1697511,
        "commercial_consumption_mwh": 1785038,
        "ind_consumption_mwh": 844387
    },
    {
        "county_name": "San Mateo County",
        "population": 754748,
        "employment": 748502,
        "res_consumption_mwh": 1452514,
        "commercial_consumption_mwh": 2251062,
        "ind_consumption_mwh": 231609
    },
    {
        "county_name": "Santa Clara County",
        "population": 1885056,
        "employment": 2043496,
        "res_consumption_mwh": 3626898,
        "commercial_consumption_mwh": 5451994,
        "ind_consumption_mwh": 3194806
    },
    {
        "county_name": "Sonoma County",
        "population": 497776,
        "employment": 335792,
        "res_consumption_mwh": 1049428,
        "commercial_consumption_mwh": 1348600,
        "ind_consumption_mwh": 845037
    },
    {
        "county_name": "Stanislaus County",
        "population": 530561,
        "employment": 278059,
        "res_consumption_mwh": 1539817,
        "commercial_consumption_mwh": 1733546,
        "ind_consumption_mwh": 1276301
    },
    {
        "county_name": "Tulare County",
        "population": 455769,
        "employment": 189068,
        "res_consumption_mwh": 1099103,
        "commercial_consumption_mwh": 965514,
        "ind_consumption_mwh": 1416291
    },
    {
        "county_name": "Ventura County",
        "population": 843110,
        "employment": 512752,
        "res_consumption_mwh": 1756132,
        "commercial_consumption_mwh": 1926500,
        "ind_consumption_mwh": 1244879
    }
]

class County:
    def __init__(self, county_name, population, employment,
                 res_consumption_mwh, commercial_consumption_mwh, ind_consumption_mwh):
        self.county_name = county_name
        self.population = population
        self.employment = employment
        self.res_consumption_mwh = res_consumption_mwh
        self.commercial_consumption_mwh = commercial_consumption_mwh
        self.ind_consumption_mwh = ind_consumption_mwh

    def total_consumption(self):
        return (
            self.res_consumption_mwh +
            self.commercial_consumption_mwh +
            self.ind_consumption_mwh
        )

    def __repr__(self):
        return f"County({self.county_name!r}, pop={self.population}, emp={self.employment})"