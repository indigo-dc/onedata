# Onedata

This is the main repository of [Onedata](http://onedata.org) - a global data management system, providing easy access to distributed storage resources, supporting wide range of use cases from personal data management to data-intensive scientific computations.

Onedata is composed of several components:

  * [Onezone](https://onedata.org/docs/doc/administering_onedata/onezone_overview.html) - allows to connect multiple storage providers into a larger distributed domain and provides users with Graphical User Interface for data management,
  * [Oneprovider](https://onedata.org/docs/doc/administering_onedata/provider_overview.html) - the main data management component of Onedata, deployed at each storage provider site, is responsible for unifying and controlling access to data over low level storage resources of the provider,
  * [Oneclient](https://onedata.org/docs/doc/using_onedata/oneclient.html) - command line tool which enables transparent access to users data spaces through [Fuse](https://github.com/libfuse/libfuse) virtual filesystem,
  * [Onepanel](https://onedata.org/docs/doc/administering_onedata/onepanel_overview.html) - administration and configuration interface for **Onezone** and **Oneprovider** components,
  * [LUMA](https://onedata.org/docs/doc/administering_onedata/luma.html) - service which allows mapping of between Onedata user accounts and local storage ID's.

This repository combines these components into one source package, which can be build and tested using single build script. Each of the components consists of the following submodules of this repository

## Common components

| Submodule | URL      | Description |
|----------------------|---------------------|-------------------------|
| **Cluster Manager** | https://github.com/onedata/cluster-manager | Common Onedata component shared between Onezone and Oneprovider, which monitors and controls Onedata worker processes at site level. |
| **Cluster Worker** | https://github.com/onedata/cluster-worker | Common Onedata worker process implementation, shared between Onezone and Oneprovider. |

## Onezone

| Submodule | URL      | Description |
|-----------|----------|--------------|
| **Onezone worker** | https://github.com/onedata/oz-worker | Main Onezone functional component, based on the **Cluster Worker** framework. |

## Oneprovider

| Submodule | URL      | Description |
|-----------|----------|--------------|
| **Oneprovider worker** | https://github.com/onedata/op-worker | Main Oneprovider functional component, based on the **Cluster Worker** framework. |

## Oneclient

| Submodule | URL      | Description |
|-----------|----------|--------------|
| **Oneclient** | https://github.com/onedata/oneclient | Oneclient command line tool implementation. |

## LUMA

| Submodule | URL      | Description |
|-----------|----------|--------------|
| **LUMA** | https://github.com/onedata/luma | Local User MApping service reference implementation. |

## Other

| Submodule | URL      | Description |
|-----------|----------|--------------|
| **Appmock** | https://github.com/onedata/appmock |  Appmock is used during testing to mock any service which exposes REST API. |
| **Bamboo scripts** | https://github.com/onedata/bamboos | Bamboos is used for automating test deployments in (bamboo)[https://www.atlassian.com/software/bamboo] during Onedata integration tests. |
| **Tests** | https://github.com/onedata/tests | Main Onedata tests repository |

>In order to initialize all submodules please use:
>```bash
>make submodules
>```
>instead of directly invoking Git `submodule` commands.

## Getting Started

The easiest way to get started with using or deploying Onedata is to start with our official [documentation](https://onedata.org/docs/index.html).

In order to try deploying Onedata, or specific components we have prepared a set of [example configurations and scenarios](https://github.com/onedata/getting-started).

## Building

This repository can be used to build entire Onedata system by simply invoking:

```bash
make
```

## Support

For support and discussion please contact as at our public [HipChat channel](https://www.hipchat.com/g3ST0Aaci), or for specific bug reports or feature requests post GitHub issues.

More information about support can be found [here](https://onedata.org/support).

