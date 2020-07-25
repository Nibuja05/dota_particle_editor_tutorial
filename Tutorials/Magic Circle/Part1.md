back to the [Tutorials](../../Tutorials.md).

# Part 1: Creating the circle

In this first part we're going to create the base effect: a spinning magic circle on the ground:

![](https://i.imgur.com/cypsRRb.gif)

## The basics

First of all let's create a new particle effect. We won't use any other resource, so we start with completly fresh and empty Particle Editor. To so open the Editor and press *Ctrl + N* to create a new particle effect.
It's good practice to save the effect at the start, so let's save this effect (pressing *Ctrl + Shift + S*) right away. It is also recommended to create a new folder for this effect and all its children. So we create a folder named `magic_circle` and save this file there with the name `magic_circle.vpcf`.

Now we want to add the bare minimum of functions we need for this particle to function. So we need an emitter, some decay and a render sprites.

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><b>Basic Functionality</b></summary>

- Since we want to create an instant effect, we need:
`Emit instantaneously` with `num to emit` set to 1 (we only want one ring).
- we want `Position within sphere random` to place our particle at CP0. Leave it at default properties.
- as always we want to have `Lifespan decay`
- also we want `Render sprites`.
- we want to set `max particles` in the Base Properties to 1, since we only need one particle here.

If you added enything else deactivate it for now. You can later active it again, if we reach the corresponding part in this tutorial.
</details>

Now we want our sprite to be better visible. So for now just increase the radius attribute in the Base Properties (*> 100 is recommended*). Next it's time to change the orientation of the sprite. We want it to ne aligned to ground instead of our screen. To do this we change the `orientation type` in Render sprites to `World-Z Align`.

## Finding the right texture

Now that we can already display a sprite on the ground, we want to change it into a proper magic circle. Since we want this effect to be extraordinary, it's recommended to use a new texture. How you do so is described below. If you don't want to do this for now, read the other option below:

<details>
  <summary><b>Creating your own texture</b></summary>
  
Importing your own texture into dota is fairly easy. All you need for that is a source image in the Targa (*.tga*) file format with transparent or black background and the [Dota2 Modkit](https://github.com/n-gao/LegionTD-Reborn-Modkit).
You can either use a new texture or use the one provided in the material folder. You can also find a version of the Dota2 Modkit there: [Materials](./materials).

If you are new to the Modkit, here is a very brief introduction: Run the *D2ModKit.exe* after you unzipped the rar folder. Enter your dota path, so the tool can find your addons. Click on the big button on the left to select the addon you're currently working in.

So if you've got everything ready, we start by copying our source image into our content folder. You can quick-open the content folder by clicking in the `C` button in the Modkit. We want to have the new texture to be in the materials folder and save it there. The file should meet following requirements:

- targa file type (*.tga*)
-  meaningful name without spaces and capital letters (*e.g. "magic_circle_01"*)
- image resolution of 2^x, so 64x64, 128x128, ..., 2048x2048
- transparent background (better) OR
- black background with white accents (black will be invisible)

Once you've copied you file there click on `T2` in the Modkit and then on `.tga -> .vtex_c`. Select your image and confirm. You have succesfully created an own texture! If you enable `Compiled Textures` and `Targa` as Asset Types in your Asset Browser, you should now see these new textures.

Now select this as the texture for Render sprites.

</details>

OR

<details>
	<summary><b>Use an existing texture</b></summary>

Open your Render sprites and change the texture. You use anything you want, but some decent looking ones can be found when searching for "rune".

</details>

Now you should have a magic circle particle displayed: 

![](https://i.imgur.com/VFXS1ob.png)

## More effects

Let's add some more effects, so the effect looks more interesting! To do so we have a lot of options: We could change the color, fade it in and many more. Try to get close to the gif at the [beginning](#part-1-creating-the-circle)

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><b>Advanced Functionality</b></summary>

- add a coloring:
	- either change the color under Base Properties
	- or add `Color random`
	- use strong intense colors to make it clearly visible ingame
- add `Alpha fade in simple` and adjust the `fade in time` to your liking
- add `Alpha fade out simple` and adjust the `fade in time` to your liking
- add `Radius scale` and set the `radius start scale` to 0. Reduce the `end time` to a lower value like 0.15. Increase the `scale bias` for a nice smooth effect
- add a spinning effect by adding `Rotation speed random`. Set the offset to something like -45 and disable the random flip direction. Also make sure you've also added `Rotation basic`!
- adjust the color: open `Color and alpha adjustments` under Render sprites. Increase the `overbright factor` to a slightly higher value like 2. This option increases the the saturation and brightness and makes the particle better visible ingame.
</details>

## Make it scaling

In the end we want to have two scaling CPs for this particle effect:

- CP1: scale duration (x-coordinate)
- CP2: scale radius (x-coordinate)
- CP0: set position

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><b>Scaling Functionality</b></summary>

duration scaling:

- add `Remap control point to scalar` 
- set the CP number to 1
- set the output field to `Life Duration`
- adjust input/output maximum to a higher number like 30 (*or whatever you want to be the maximum duration*)

radius scaling:

- add `Remap control point to scalar` 
- set the CP number to 2
- set the input/output maximum to a high number like 5000
- enable `Visualize` and `Show control points` and set the x-coordinate of CP2 to something like 2000
- check if the CP2 marker is directly on the outer edge of the ring
- if not adjust the output maximum, until it matches
- now the radius scaled correctly with the visuals

</details>

## Move on

We're done with the fundamentals. In the next part we're going to create a child effect, that add some sparks and focuses on interesting movement possibilities.

[<< Previous <<](./Introduction.md) - [Introduction](./Introduction.md) - [Part 1](#) - [Part 2](./Part2.md) - [Part 3](./Part3.md) - [Part 4](./Part4.md) - [Part 5](./Part5.md) - [>> Next >>](./Part2.md)
