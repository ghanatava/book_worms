pipeline{

  agent any
  stages{
    stage('check requirements'){
        steps{
            sh ''' 
                docker --version
                docker compose version
                curl --version
            '''
        }
    }

    stage('run contianers'){
        steps{
            sh 'docker system prune -a --volumes -f'
            sh 'docker compose up -d'
            sh 'docker ps'
        }
    }

    stage('testing'){
        steps{
            sh 'sleep 10'
            sh 'curl http://localhost:8000'
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