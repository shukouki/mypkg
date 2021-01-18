# mypkg
## ロボットシステム学　課題２　ROS

## 内容 

千葉工業大学ロボットシステム学第10回のコードを参考に作成したものです。

- 講義内ではノードcount.pyによってパブリッシャcount_upに1ずつ増加するデータをノードtwice.pyによって2倍し、パブリッシャtwiceに出力する内容でした。
- ノードcount.pyによってパブリッシャcount_upに2ずつ増加するデータを出力する変更をしました。 
- ノードsum.pyによってパブリッシャsumにcount_upの値の合計を逐一出力する内容を加えました。

## 実演動画

## 環境

| | |
|:--:|:--:|
|OS|ubuntu 20.04|
|ROS|noetic|

## 準備

  [講義で用いたROSのインストール](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server) 
  
  - 環境構築 
  '''
  $ cd
  $ mkdir -p catkin_ws/src
  $ cd ~/catkin_ws/src
  $ catkin_init_workspace 
  Creating symlink "/home/ubuntu/catkin_ws/src/CMakeLists.txt" pointing to 
  "/opt/ros/melodic/share/catkin/cmake/toplevel.cmake"
  $ ls
  CMakeLists.txt
  '''
  
  - .bashrcの末尾に以下を記述
  source /opt/ros/noetic/setup.bash          #これは元からある
  source ~/catkin_ws/devel/setup.bash         #ここから3行追加
  export ROS_MASTER_URI=http://localhost:11311
  export ROS_HOSTNAME=localhost
  
  - 環境構築つづき
  $ cd ~/catkin_ws/src
  $ git clone https://github.com/shukouki/mypkg.git
  $ cd ~/catkin_ws
  $ catkin_make
  $ source ~/.bashrc
    
## 実行方法 
    -端末1(ROS起動) 
    $ roscore
    
    -端末2(count.pyの実行) 
    $ cd ~/catkin_ws/src/mypkg/scripts/
    $ rosrun mypkg count.py
    
    -端末3(count_upへの出力を確認) 
    $ rostopic echo /count_up
    
    -端末4(sum.pyの実行) 
    $ cd ~/catkin_ws/src/mypkg/scripts/
    $ rosrun mypkg sum.py
    
    -端末5(sumへの出力を確認) 
    $ rostopic echo /sum
    

## 参考 
  
  - 上田隆一先生による講義内容のリポジトリ
  https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md
  
  - 講義動画
  https://www.youtube.com/watch?v=PL85Pw_zQH0&t=3481s
  
  - ROSwiki
  http://wiki.ros.org/ja
  
  - TAさんのリポジトリ
  https://github.com/GakuKuwano/robosys2020_ros

## ライセンス
