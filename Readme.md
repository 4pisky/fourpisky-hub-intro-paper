# Paper: *The 4 Pi Sky transient alerts hub*
A paper giving an overview of the 4 Pi Sky software packages and subsystems, covering:
- [voevent-parse](https://github.com/timstaley/voevent-parse/)
- [fourpiskytools](https://github.com/4pisky/fourpiskytools)
- [voeventdb](https://github.com/timstaley/voeventdb)
- [fourpisky-core](https://github.com/4pisky/fourpisky-core)
- and related deployment scripts, e.g. [4pisky-voeventdb](https://github.com/4pisky/4pisky-voeventdb)

## Abstract
We introduce the 4 Pi Sky 'hub', a collection of open data-services and underlying software packages built for rapid, fully automated reporting and response to astronomical transient alerts. 
These packages build on the mature 'VOEvent' standardized message-format, and aim to provide a decentralized and open infrastructure for handling transient alerts. 
In particular we draw attention to the initial release of *voeventdb*, an archive and remote-query service that allows astronomers to make historical queries about transient alerts. 
By employing spatial filters and web-of-citation lookups, voeventdb enables cross-matching of transient alerts to bring together data from multiple sources, as well as providing a point of reference when planning new follow-up campaigns.
We also highlight the recent addition of optical-transient feeds from the ASASSN and GAIA projects to our VOEvent distribution stream.
Both the source-code and deployment-scripts which implement these services are freely available and permissively licensed, with the intention that other teams may use them to implement local or project-specific VOEvent archives. 
In the course of describing these packages we provide a basic primer for getting started with automated transient astronomy, including a condensed introduction to the VOEvent standard.
