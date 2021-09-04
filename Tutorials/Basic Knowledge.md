<p>back to the <a href="../Tutorials.md">Tutorials</a>.</p>
<h1 id="basic-knowledge">Basic Knowledge</h1>
<p>In this short text we will look at a few simple points dealing mainly with the structure and organization of particle effects.</p>
<h2 id="directory-structure">Directory Structure</h2>
<p>Especially with more complex and multi-child particle effects, the file structure can get quite messy if not managed properly. So here are some important points, you should keep in mind:</p>
<ul>
<li>Even if you don’t plan to create a lot of particles, its still advisable to start with a well defined directory structure. Its easier to set it up correctly than changing it later on</li>
<li>Group particles based on common usage in the root particle directory. E.g. create a folder named <code>heroes</code> or <code>units/heroes</code> for hero particles or <code>ambient</code> for particles used in hammer. You can structure it any way you like, but keeping it organized is quite important.</li>
<li>Create a new directory for more complex particles. If you know that the particle effect you are working on will probably have a lot of children, don’t hesitate in creating a new folder for it. E.g. you can group all particle effect for each ability of a hero in a single folder.</li>
<li>Use <code>snake_case</code> for you particle naming. Valve uses this for all their particles, so it’s best to keep it this way.</li>
<li>Keep a clear name for the the root/parent particle. The particle you want to refer later in the code should be named as simple as possible so it will be easy to use and remember. E.g. a particle effect for the ability <code>tinker_death_laser</code> could be named <code>death_laser</code>.</li>
<li>Name child particles based on their parent. Lets assume you particle is called <code>death_laser</code>. It’s children should be named after their parent  + <code>_</code> + additional function. So in this example it could have children named (some common used terms) <code>death_laser_endcap</code>, <code>death_laser_impact</code>, <code>death_laser_body</code>, <code>death_laser_sparks</code>, etc. If you have similiar particles you can also “numerate” them. It’s advised to use alphabetical order: <code>death_laser_sparks_a</code>, <code>death_laser_sparks_b</code>, etc.</li>
<li>If you want to change the path of a particle later on, you can’t simply copy paste it to another location, since all child/parent paths are not necessarily relative. For this purpose you can open the particle system you want to move/copy and go to <strong>File &gt; Copy System Definition…</strong> With this tool you are able to maintain all functionility while copying the particle effects.</li>
</ul>
<h2 id="control-points">Control Points</h2>
<p>It is also very important that you manage your control points of any particle effect you create wisely. Since most particle effects are made by valve, it’s advised to maintain their default way of CP usage.</p>
<ul>
<li><strong>CP0</strong>: This is the most used control point. CP 0 should always be used for the placement of particle effects. If you have something that moves, CP 0 should always be the start point.</li>
<li><strong>CP1</strong>: This control point is used differently based on particle behavior: If you need a second control point to indicate a position, use CP 1. If you don’t have any other position besides CP 0 that you need, this CP can be used for any value.</li>
<li><strong>CP2</strong>: Basically the same as CP 1, but more often used for values rather than a position, since most particle effects don’t need more than 2 positions at most. Only use this CP, if CP 1 is already used.</li>
<li><strong>CP3</strong>: This CP indicated a moving position, often transferred to child effects. If you want a child particle to move along your particles, use CP 3. Most projectile endcap effects use this as their origin.</li>
<li><strong>CP 4-59</strong>: You are free to use these CPs for anything else you might need</li>
<li><strong>CP 60-62</strong>: These CPs are reserved for the usage of <em>HSV Shift to control points</em> (Color adjustments, introduced for Rubick Arcana). Simply don’t use these, you probably have anough other CPs to use.</li>
</ul>
<p>Some special cases here:</p>
<h4 id="linear-projectiles">Linear Projectiles</h4>
<ul>
<li><strong>CP0</strong>: Start position</li>
<li><strong>CP1</strong>: Velocity</li>
<li><strong>CP3</strong>: Automatically set. Used for current projectile position</li>
</ul>
<h4 id="tracking-projectiles">Tracking Projectiles</h4>
<ul>
<li><strong>CP0</strong>: Start position</li>
<li><strong>CP1</strong>: End position</li>
<li><strong>CP2</strong>: X-coordinate: speed</li>
<li><strong>CP3</strong>: Automatically set. Used for current projectile position</li>
</ul>
<h2 id="asset-browser">Asset Browser</h2>
<p>Even if you organized you particles perfectly directory-wise, you might still have some problems with finding your particles in the asset browser. You can simply type the full name, but you have  alot more options:</p>
<ul>
<li>On the top right you have the option to select several perferences:<br>
<img src="https://i.imgur.com/CAjoKeQ.png" alt=""><br>
<strong>Tags</strong> are mostly useless, so ignore that for now. With <strong>Mods</strong> you decide whether the Asset Browser is displaying only particles from your addon, only default dota particles or both. <strong>Asset Types</strong> is most important as it can filter file types. You mostly want to see <em>Particle System</em> or sometimes <em>Model</em>.</li>
<li>Another very useful feature are <strong>Saved Searches</strong>. You can find the button for that on top:  <img src="https://i.imgur.com/jhZDXM9.png" alt=""><br>
If you click on the <strong>New</strong> Button here, it will save your  last search you did. This includes: <em>Mods</em>, <em>Asset Types</em>, <em>Search String</em> etc.<br>
This is a very useful feature that can save a lot of time and is saved across multiple sessions.<br>
*<em>Note: These saves will create a file named <code>AssetBrowserSavedSearches.kv3</code>, that can be shared and modified too</em>.</li>
<li>You can also use advanced search strings. There is a convenient help button by default: <img src="https://i.imgur.com/8yokcoN.png" alt=""></li>
<li>You can also create <strong>Working Sets</strong>. To do so, select multiple assets at once (<em>Shift</em>/<em>Ctrl</em> + click) and then use right click and select <em>Create New Working Set</em> to store the selected assets in a working set. It will then be shown in the top bar: <img src="https://i.imgur.com/MiAR3md.png" alt="enter image description here"><br>
You can also remove assets from the currently selected workset from the right click context menu.<br>
<em>Note: It’s not possible to add assets to an existing working set, so only use with care!</em>*</li>
<li>Another very useful feature is <strong>Visualize References</strong> (right click context menu). This will show you a graph of all assets connected to the selected one.<br>
<img src="https://i.imgur.com/nAvFP28.png" alt=""><br>
This is especially useful if you don’t want to open the asset and still check what it depends on, or to view all usages of models/materials what would be impossible otherwise. On the right below the preview are even more options:<br>
<img src="https://i.imgur.com/FGh9B1X.png" alt=""></li>
<li>An often overlooked but useful feature is also <strong>Set Name Filter</strong> that can be activated from the right click context menu. It will replace your current search string with a new search query, that shows similar assets. It works quite well for valve particles and will also work great for custom particles, if they are named accordingly.</li>
</ul>
<h2 id="particle-editor">Particle Editor</h2>
<p><em>(short: PE)</em><br>
I will not talk about the Particle Editor here in detail, since I covered most the things to say already in the <a href="../Particle%20Editor%20Guide.md">Particle Editor Tutorial</a>. I will only hint to some features that might be of interest too:</p>
<ul>
<li>Each Operator also has <strong>Hidden Attributes</strong>. Most of the operators have the same, but renderes and the base properties have special stuff too. To show these hidden attributes, you can use the setting icon here:<br>
<img src="https://i.imgur.com/5IbV13b.png" alt=""></li>
<li>You can also enable the <strong>Raw Edit Mode</strong> like that. This will show all operator field names without their localization (only english). This feature is only useful, if you want to do anything with direct particle file manupulation, so it will be used only very rarely.</li>
</ul>

