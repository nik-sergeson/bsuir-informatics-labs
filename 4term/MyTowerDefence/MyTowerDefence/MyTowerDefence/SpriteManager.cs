using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using System.IO;


namespace MyTowerDefence
{
    public class SpriteManager : Microsoft.Xna.Framework.DrawableGameComponent
    {
        private SpriteBatch spriteBatch;
        private SpriteFont spritefont;
        private UserControlledSprite player;
        private List<Building> towerlist = new List<Building>();
        private List<Enemy> enemies;
        private Map map;
        private int nextSpawnTime = 0;
        private int count;
        private int bonusmoney;
        private Menu menu;
        private void ResetSpawnTime()
        {
            nextSpawnTime = 5000;
        }

        public SpriteManager(Game game): base(game)
        {
            count = 10;
            bonusmoney = 0;
        }

        public override void Initialize()
        {
            base.Initialize();
        }

        public override void Update(GameTime gameTime)
        {
            MouseState currMouseState = Mouse.GetState();
            if (player != null)
                player.Update(gameTime);
            KeyboardState curkey = Keyboard.GetState();
            if (curkey.GetPressedKeys().Contains(Keys.F12))
            {
                GameSaver<List<Building>>.Save(towerlist, "towers.dat");
                GameSaver<Menu>.Save(menu, "menu.dat");
                GameSaver<List<Enemy>>.Save(enemies, "enemies.dat");
            }
            if (currMouseState.LeftButton == ButtonState.Pressed)
            {
                if (player.towerischosen==false)
                {
                    menu.ChooseItem(currMouseState.X, currMouseState.Y,player);
                }
                else if (currMouseState.X <= map.collisionRect.Width)
                {
                    Vector2 vec = map.PlaceTower(currMouseState.X,currMouseState.Y,20,20,towerlist);
                    if (vec != Vector2.Zero)
                    {
                        if (player.curtower == BuildingType.AntiAerienne)
                            towerlist.Add(new AntiAerinne(Game.Content.Load<Texture2D>(@"Images/Towers/tourAntiAerienne"), Game.Content.Load<Texture2D>(@"Images/Bullet"), vec.X, vec.Y, (float)0.1,@"Images/Towers/tourAntiAerienne",@"Images/Bullet"));
                        else if (player.curtower == BuildingType.Archer)
                            towerlist.Add(new Archer(Game.Content.Load<Texture2D>(@"Images/Towers/tourArcher"), Game.Content.Load<Texture2D>(@"Images/Bullet"), vec.X, vec.Y, (float)0.1,@"Images/Towers/tourArcher",@"Images/Bullet"));
                        else
                            towerlist.Add(new DeFeu(Game.Content.Load<Texture2D>(@"Images/Towers/tourDeFeu"), Game.Content.Load<Texture2D>(@"Images/Bullet"), vec.X, vec.Y, (float)0.1,@"Images/Towers/tourDeFeu",@"Images/Bullet"));
                        player.towerischosen = false;
                    }
                }
            }
            else if(currMouseState.RightButton==ButtonState.Pressed)
                menu.ShowInfo(currMouseState.X, currMouseState.Y);
            if (menu.gamestate != GameState.Paused)
            {
                for (int i = 0; i < enemies.Count; i++)
                {
                    if (enemies[i].HealthPoint <= 0)
                    {
                        bonusmoney += enemies[i].cost;
                        enemies.RemoveAt(i);
                        i--;
                    }
                    else if (enemies[i].AtFinishPoint == true)
                    {
                        enemies.RemoveRange(0, enemies.Count);
                        menu.gamestate = GameState.GameOver;
                        break;
                    }
                    else
                        enemies[i].Update(gameTime);
                }
                menu.Update(bonusmoney, count);
                bonusmoney = 0;
                if (menu.gamestate == GameState.Reset)
                {
                    menu.gamestate = GameState.Paused;
                    ReserGame();
                }
                if (enemies.Count == 0&&count==0&&menu.gamestate!=GameState.GameOver)
                    menu.gamestate = GameState.PlayerWon;
                if (menu.gamestate == GameState.Started)
                {
                    foreach (var s in towerlist)
                    {
                        if (enemies.Count != 0)
                            s.Attack(enemies);
                        s.Update(gameTime);
                    }
                    nextSpawnTime -= gameTime.ElapsedGameTime.Milliseconds;
                    if ((nextSpawnTime < 0) && (count != 0))
                    {
                        SpawnEnemy();
                    }
                }
            }
            base.Update(gameTime);
        }

        public override void Draw(GameTime gameTime)
        {
            spriteBatch.Begin(SpriteSortMode.BackToFront, BlendState.AlphaBlend);
            map.Draw(spriteBatch);
            if (player.towerischosen==true)
                player.Draw(spriteBatch);
            foreach (var enemy in enemies)
                enemy.Draw(spriteBatch);
            foreach (Building s in towerlist)
                s.Draw(spriteBatch);
            menu.Draw(spriteBatch, spritefont);
            spriteBatch.End();
            base.Draw(gameTime);
        }

        protected override void LoadContent()
        {
            spritefont = Game.Content.Load<SpriteFont>(@"Fonts\Font");
            spriteBatch = new SpriteBatch(Game.GraphicsDevice);
            List<StaticTower> towicons = new List<StaticTower>();
            towicons.Add(new StaticTower(Game.Content.Load<Texture2D>(@"Images/Towers/icone_tourAntiAerienne"), new Vector2(500, 20), (float)0.1, Game.Content.Load<Texture2D>(@"Images/Towers/icone_tourAntiAerienne"),BuildingType.AntiAerienne));
            towicons.Add(new StaticTower(Game.Content.Load<Texture2D>(@"Images/Towers/icone_tourArcher"), new Vector2(564, 20), (float)0.1, Game.Content.Load<Texture2D>(@"Images/Towers/icone_tourArcher"),BuildingType.Archer));
            towicons.Add(new StaticTower(Game.Content.Load<Texture2D>(@"Images/Towers/icone_tourDeFeu"), new Vector2(628, 20), (float)0.1,Game.Content.Load<Texture2D>(@"Images/Towers/icone_tourDeFeu"),BuildingType.DeFeu));
            Texture2D towbckgrd = Game.Content.Load<Texture2D>(@"Images/GreyButton");
            List<StaticSprite> background = new List<StaticSprite>();
            background.Add(new StaticSprite(towbckgrd, new Vector2(476, 8),(float)0.5));
            background.Add(new StaticSprite(towbckgrd, new Vector2(540, 8), (float)0.5));
            background.Add(new StaticSprite(towbckgrd, new Vector2(604, 8), (float)0.5));
            List<MenuButton> menubuttons = new List<MenuButton>();
            menubuttons.Add(new MenuButton(Game.Content.Load<Texture2D>(@"Images/PauseButton"),new Vector2(486,300),(float)0.1,GameState.Paused));
            menubuttons.Add(new MenuButton(Game.Content.Load<Texture2D>(@"Images/PlayButton"), new Vector2(550, 300), (float)0.1, GameState.Started));
            menubuttons.Add(new MenuButton(Game.Content.Load<Texture2D>(@"Images/ResetButton"), new Vector2(614, 300), (float)0.1, GameState.Reset));      
             List<Vector2> road = new List<Vector2>();
            road.Add(new Vector2(140, 0));
            road.Add(new Vector2(140, 50));
            road.Add(new Vector2(58, 50));
            road.Add(new Vector2(58, 180));
            road.Add(new Vector2(280, 180));
            road.Add(new Vector2(280, 300));
            road.Add(new Vector2(58, 300));
            road.Add(new Vector2(58, 420));
            road.Add(new Vector2(410, 420));
            road.Add(new Vector2(410, 60));
            road.Add(new Vector2(270, 60));
            road.Add(new Vector2(270, 0));
             enemies = new List<Enemy>();
             if (File.Exists("enemies.dat") && File.Exists("menu.dat") && File.Exists("towers.dat"))
             {
                 enemies = GameSaver<List<Enemy>>.Read("enemies.dat");
                 foreach (var en in enemies)
                 {
                     en.UpdateTexture(Game, GraphicsDevice);
                 }
                 menu = GameSaver<Menu>.Read("menu.dat");
                 menu.Reload(towicons, menubuttons, background);
                 towerlist = GameSaver<List<Building>>.Read("towers.dat");
                 foreach (var tow in towerlist)
                     tow.UpdateTexture(Game);
                 bonusmoney = 0;
                 count = menu.EnemyCount;
                 File.Delete("menu.dat");
                 File.Delete("towers.dat");
                 File.Delete("enemies.dat");
             }
             else
             {
                 menu = new Menu(towicons, menubuttons, background);
                 menu.Update(30, count);
             }
            map = new Map(Game.Content.Load<Texture2D>(@"Images/elementTD"), Vector2.Zero, road,(float)0.9);
            player = new UserControlledSprite(null, Vector2.Zero, Vector2.Zero, 0);
            base.LoadContent();
        }

        private void SpawnEnemy()
        {
            Vector2 speed= new Vector2(0, (float)2.2);
            Vector2 position = new Vector2(140,0);
            if(count>=7)
                enemies.Add(new Eagle(Game.Content.Load<Texture2D>(@"Images/Monster/aigle"), GraphicsDevice, position, (float)0.1, map.road, @"Images/Monster/aigle"));
            else if(count>=4)
                enemies.Add(new Spider(Game.Content.Load<Texture2D>(@"Images/Monster/araignee"), GraphicsDevice, position, (float)0.1, map.road, @"Images/Monster/araignee"));
            else if(count>=2)
                enemies.Add(new Elephant(Game.Content.Load<Texture2D>(@"Images/Monster/elephant"), GraphicsDevice, position, (float)0.1, map.road, @"Images/Monster/elephant"));
            else
                enemies.Add(new GiantSpider(Game.Content.Load<Texture2D>(@"Images/Monster/grandeAraignee"), GraphicsDevice, position, (float)0.1, map.road,@"Images/Monster/grandeAraignee"));
            --count;
            ResetSpawnTime();
        }

        public void ReserGame()
        {
            towerlist.RemoveRange(0, towerlist.Count);
            enemies.RemoveRange(0, enemies.Count);
            count = 10;
            bonusmoney = 0;
            menu.money = 0;
            menu.Update(30, count);
            nextSpawnTime = 0;
        }
    }
}
