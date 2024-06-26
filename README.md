<br />
<div align="center" id="readme-top">
  <h2 align="center">Pyssword Manager</h2>
  <p align="center">
    <a href="https://github.com/HassenH1/pyssword-manager/issues">Report Bug</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [pyssword-manager-image]: assets/pysswordmanagerimage.png

![pyssword-manager-image] -->

<p align="center" width="100%">
    <img width="80%" src="assets/pysswordmanagerimage.png" />
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[PYTHON]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

![PYTHON]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Make sure you have node installed

### Installation

1. Clone the repo

```sh
git clone https://github.com/HassenH1/pyssword-manager .
```

2. Create virtual env

```sh
python -m venv vitrualenv
```

3. Active virtual env

```sh
\virtualenv\Scripts\Activate.ps1
```

> **_NOTE:_** to deactivate virtual env when you are finished, you can run
>
> ```sh
> deactivate
> ```

4. Install all the dependecies

```sh
pip install -r requirements.txt
```

5. Run database container

```sh
docker-compose up
```

> **_NOTE:_** to halt and remove container when you are finished, you can run
>
> ```sh
> docker-compose down
> ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Replace password string with \*
- [ ] Use crypto for stronger password generator
- [ ] Use singleton pattern for database class
- [ ] Integrate database to application
- [ ] Fix bugs

<!-- No roadmap currently -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Hassen Hassen - [LinkedIn](https://www.linkedin.com/in/hassenhassen/) - hasansaid51@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>
