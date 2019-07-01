# Thesis common modules

## Description

Project which contains dependencies used in few developed projects:

- [Noise Detection CNN](https://github.com/prise-3d/Thesis-NoiseDetection-CNN.git)
- [Denoising autoencoder](https://github.com/prise-3d/Thesis-Denoising-autoencoder.git)
- [Noise Detection attributes](https://github.com/prise-3d/Thesis-NoiseDetection-attributes.git)
- [Noise Detection 26 attributes](https://github.com/prise-3d/Thesis-NoiseDetection-26-attributes.git)

## Configuration file

There is few configuration files (`config` folder):
- **global:** contains common variables of project
- **attributes:** extends from global and contains specific variables
- **cnn:** extends from global and contains specific variables for Deep Learning

## Add as dependency

```bash
git submodule add https://github.com/prise-3d/Thesis-CommonModules.git modules
```

## License

[The MIT License](https://github.com/prise-3d/Thesis-CommonModules/blob/master/LICENSE)