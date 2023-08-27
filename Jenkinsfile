pipeline{

  agent any
  stages{
    stage('check requirements'){
        steps{
            sh ''' 
                docker --version
                docker compose --version
                curl --version
            '''
        }
    }

    stage('run contianers'){
        steps{
            sh 'docker compose up -d --no-color'
        }
    }

    stage('testing'){
        steps{
            sh 'curl http://localhost:8000 > '
        }
    }
  }
 
  post{
    always{
        sh 'docker compose down --remove-orphans -v'
        sh 'docker compose ps'
    }
  }
}