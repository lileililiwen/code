<?php

class ChatBotAggregator {
  private $bots; // 所有机器人列表
  private $retryLimit; // 重试次数限制

  public function __construct($bots, $retryLimit = 2) {
    $this->bots = $bots;
    $this->retryLimit = $retryLimit;
  }

  public function sendMessage($userMessage) {
    // 根据优先级排序机器人列表
    $sortedBots = $this->sortBotsByPriority($this->bots);

    // 初始化重试次数
    $retryCounts = array_fill_keys(array_keys($sortedBots), 0);

    // 循环尝试机器人直到成功响应或达到重试次数限制
    foreach ($sortedBots as $bot) {
      while ($retryCounts[$bot] <= $this->retryLimit) {
        $response = $this->bots[$bot]->sendMessage($userMessage);
        if ($response) {
          return $response;
        } else {
          $retryCounts[$bot]++;
        }
      }
    }

    // 如果所有机器人都没有成功响应，返回默认响应
    return "I'm sorry, I couldn't understand your message.";
  }

  private function sortBotsByPriority($bots) {
    $sortedBots = array_keys($bots);
    usort($sortedBots, function($bot1, $bot2) use ($bots) {
      return $bots[$bot2]->getPriority() - $bots[$bot1]->getPriority();
    });
    return $sortedBots;
  }
}

interface ChatBot {
  public function getPriority();
  public function sendMessage($userMessage);
}

class SimpleChatBot implements ChatBot {
  private $priority;
  private $responses;

  public function __construct($priority, $responses) {
    $this->priority = $priority;
    $this->responses = $responses;
  }

  public function getPriority() {
    return $this->priority;
  }

  public function sendMessage($userMessage) {
    // 简单的响应逻辑，直接根据用户消息返回对应响应
    if (isset($this->responses[$userMessage])) {
      return $this->responses[$userMessage];
    } else {
      return null;
    }
  }
}

// 示例用法：
$bots = array(
  'weatherBot' => new SimpleChatBot(10, array(
    'What is the weather like today?' => 'It is sunny today.',
    'Is it going to rain tomorrow?' => 'Sorry, I do not have information for tomorrow.'
  )),
  'newsBot' => new SimpleChatBot(5, array(
    'What is the latest news?' => 'The latest news is about the stock market.',
    'Tell me about the political situation.' => 'Sorry, I do not have information on that topic.'
  ))
);

$chatBot = new ChatBotAggregator($bots, 2);

echo $chatBot->sendMessage('What is the weather like today?') . "\n"; // It is sunny today.
echo $chatBot->sendMessage('Tell me about the political situation.') . "\n"; // I'm sorry, I couldn't understand your message.
