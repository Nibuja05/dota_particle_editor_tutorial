---


---

<h1 id="particle-editor-tutorial">Particle Editor Tutorial</h1>
<p>The Particle Editor is a powerful tool that allows to create all kinds of particle effects, from ambient effects to projectiles up to HUD animations. So its definitely worth for everybody to learn how to create their own.<br>
Here you will learn the basics to understand the tool, as well as advanced techniques to master particle creation!</p>
<p>This is a work that is constantly being expanded with new content. So if important information is missing, you are welcome to contribute!</p>
<h2 id="contents">Contents</h2>
<ul>
<li><a href="#Tool">The Tool</a></li>
<li><a href="#Functions">Functions</a></li>
</ul>
<p><a></a></p>
<h2 id="the-tool">The Tool</h2>
<p>There are two ways to open the Particle Editor: The first is to click on the flame symbol on the top left of the main asset browser window to open a blank new window. The second way is to directly open an existing particle effect by double clicking it in the asset browser.</p>
<p>Now open an existing particle effect as an example:</p>
<h3 id="menu">Menu</h3>
<p>In the top left you have standard menu actions with File, Edit, View and Help. There’s nothing special about it and just some default operations like save, open etc.<br>
Important note here: In order to modify valves particles you need to save it in your current addon.</p>
<h3 id="preview">Preview</h3>
<p>The biggest part of your window should be filled with a preview part in the middle. There you can already see how the effect will eventually look like in the game. You can move freely with WASD, the right mouse button and the mouse wheel to see the effect from any side and distance. The symbols in the upper bar are explained in the <a href="#ToolAdvanced">advanced part</a>.</p>
<h3 id="functions">Functions</h3>
<p>The functions are the heart of every particle effect. Here you can define all properties and behaviors that make the effect what it is. In the upper part, there are also 4 small buttons that make navigation much easier. If you have more than one effect open at the same time in the particle editor, you can jump to the last displayed effect with the left arrow. Likewise, the arrow to the right leads to the next effect. The button to the right is either grayed out and shows a P or a number. If the current effect is added to another effect as a child you can use it to display a list of these effects and jump to them. Vice versa the button next to it with a number or a capital C. This shows subordinate effects in a tree structure. If these two buttons are not clickable, it means that there are no effects available at the moment.<br>
More about the functions in detail here: <a href="#Functions">Functions</a>.</p>
<h3 id="properties">Properties</h3>
<p>The detailed data for the currently selected function is displayed here. If you want to make changes to one of the functions, this is the right place to do so.</p>
<h3 id="controls">Controls</h3>
<p>The control part is divided into two parts: the control points and preview. Control points are 3-dimensional vectors that form the interface between the particle effect and the code. By clicking on the colored icon to the right of the arrow, you can directly influence these points, for example by moving or rotating them. Alternatively you can also enter your desired values in the fields next to it. On the far right you will find a small lock symbol. If it is closed, the entered values are saved, so that the next time you open this effect in the Particle Editor, the values are immediately restored to the saved values. With the preview part below, other assets like models can be loaded directly into the current effect. This is only a test tool and has no influence on the final result displayed in the game. Nevertheless, it is essential for quick testing of different effects.</p>
<p><a></a></p>
<h2 id="functions-1">Functions</h2>

