using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace MyTowerDefence
{
    public class Bullet:Sprite
    {
        private Enemy enemy;
        private int damage;
        public override Vector2 direction
        {
            get { return speed; }
        }
        
        public bool Hit(){
            return enemy.Collide(collisionRect);
        }

        public void HitEnemy()
        {
            enemy.HealthPoint -= damage;
        }

        public override void Update(GameTime gameTime) {
            position += direction;
            base.Update(gameTime);
        }

        public static Vector2 TrajectoryCalculation(Enemy enemy,int maxspeed,Vector2 position,Rectangle bulrect, int attackradius)
        {
            List<Vector2> trajectdiv = enemy.FutureCheckpoints(attackradius, position.X, position.Y);
            double r,time;
            Vector2 enemyfutpos;
            foreach (var traject in trajectdiv)
            {
                r = Math.Sqrt(Math.Pow(traject.X - position.X, 2.0) + Math.Pow(traject.Y - position.Y, 2.0));
                time = r / maxspeed;
                enemyfutpos = enemy.FuturePosition((int)time);
                if (Sprite.Collide(new Rectangle((int)(enemyfutpos.X - enemy.collisionRect.Width / 2), (int)(enemyfutpos.Y - enemy.collisionRect.Height / 2), enemy.collisionRect.Width, enemy.collisionRect.Height), new Rectangle((int)(traject.X - bulrect.Width / 2), (int)(traject.Y - bulrect.Height / 2), bulrect.Width, bulrect.Height)))
                    return new Vector2((float)(maxspeed * Math.Cos(Math.Atan2(traject.Y - position.Y, traject.X - position.X))), (float)(maxspeed * Math.Sin(Math.Atan2(traject.Y - position.Y, traject.X - position.X))));
            }
            return Vector2.Zero;
        }

        public Bullet(Texture2D textureImage, Vector2 position, Enemy enemy, int maxspeed, int attackradius, int damage, float layerdepth)
            : base(textureImage, position, TrajectoryCalculation(enemy,maxspeed,position,new Rectangle((int)position.X,(int)position.Y, textureImage.Width,textureImage.Height), attackradius),layerdepth)
        {
            this.enemy = enemy;
            this.damage=damage;
        }

        public Bullet(Texture2D textureImage, Vector2 position, Vector2 speed, Enemy enemy, int damage, float layerdepth)
            : base(textureImage, position, speed,layerdepth)
        {
            this.enemy = enemy;
            this.damage=damage;
        }
    }
}