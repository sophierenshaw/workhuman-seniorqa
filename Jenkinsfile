pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/sophierenshaw/workhuman-seniorqa.git']]])
            }
        }
        
        stage('Unit Tests'){ 
                steps{
                    dir('.') {
                        sh '. ./venv/bin/activate'
                        sh 'pip install -r requirements.txt'
                        sh 'pytest -v task1 task2 task3'
                    }           
                    }                    
                }  
    }
}