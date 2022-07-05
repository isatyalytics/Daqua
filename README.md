# DAQUA

Daqua is a data quality measurement tool. We can connect to any data source which contains tabular data to perform data profiling and various indicator for data quality for data cleaning. 

## Getting Started

To use daqua, you need to install it by using pip.

> pip install daqua

### Prerequisites

You need to have numpy and pandas installed in your system for using daqua.


### Getting started

```
# importing the package
import daqua

# Creating an object of the Daqua class
dq = daqua.Daqua()

# reading an excel file
dq.read_excel(path_to_excel)

# get the dataframe dictionary
## The structure is like {"sheet_name" : df}

dict_dfs = dq.getDataFrames()

# get meta data about the dataframe
meta = dq.getMetaData()


# get detailed metadata
detailed_meta = dq.getDetailedMeta()

# get the descriptive stat for numeric columns
descriptive_stat_dict = dq.getNumericDesc()

# get quantile stats
quant_dict = dq.getQuantileStat()
```


## Deployment

link to pypi: https://pypi.org/project/daqua/


## Contributing

Please read [CONTRIBUTING.md](link to contri page) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Satya Pati** - *Initial work* - [Github](https://github.com/PurpleBooth)
* **Lalit Moharana** - *Initial work* - [Github](https://github.com/PurpleBooth)
* **Soumya Ranjan Bisoi** - *Initial work* - [Github](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

